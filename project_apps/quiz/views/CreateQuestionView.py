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


	def form_valid(self, form):
		new_question = form.save()
		self.question_id = new_question.id
		return self.get_success_url()


	def get_success_url(self):
		return HttpResponseRedirect(reverse('quiz:create-choices', args=(self.question_id,)))