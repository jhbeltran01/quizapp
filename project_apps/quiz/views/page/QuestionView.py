from re import S
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ...forms.CreateQuestionForm import CreateQuestionForm
from ...models import Question

class QuestionView(LoginRequiredMixin, generic.ListView, generic.CreateView):
	model = Question
	form_class = CreateQuestionForm
	template_name = 'quiz/question.html'
	context_object_name = 'questions_list'


	def get(self, request, *args, **kwargs):
		self.object = None
		self.set_needed_id(kwargs)
		self.set_test_object(request)
		return super().get(request, *args, **kwargs)


	def post(self, *args, **kwargs):
		self.set_needed_id(kwargs)
		return super().post(*args, **kwargs)


	def form_valid(self, form):
		self.set_test_object(self.request)
		new_question = self.request.user.question_set.create(text=form.cleaned_data['text'])
		new_question.tests.add(self.test)
		return HttpResponseRedirect(reverse('quiz:choice', args=(self.room_id, self.test_id, new_question.id)))


	def get_queryset(self):
		return self.test.question_set.all()


	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['room_id'] = self.room_id
		context['test_id'] = self.test_id
		return context


	def set_test_object(self, request):
		self.test = request.user.room_set.get(pk=self.room_id).test_set.get(pk=self.test_id)


	def set_needed_id(self, kwargs):
		self.room_id = kwargs['room_id']
		self.test_id = kwargs['test_id']