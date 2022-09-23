from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..models import Question
from ..forms.CreateQuestionForm import CreateQuestionForm

class CreateQuestionView(LoginRequiredMixin, generic.CreateView):
	model = Question
	form_class = CreateQuestionForm
	template_name = 'quiz/create-question.html'


	def post(self, *args, **kwargs):
		self.room_id = kwargs['room_id']
		self.test_id = kwargs['pk']
		return super().post(*args, **kwargs)

	def form_valid(self, form):
		self.request.user.room_set.get(pk=self.room_id).test_set.get(pk=self.test_id).question_set.create(text=form.cleaned_data['text'])
		return HttpResponseRedirect(reverse('quiz:question-list', args=(self.room_id, self.test_id)))