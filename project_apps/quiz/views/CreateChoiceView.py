from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateChoiceView(LoginRequiredMixin, generic.TemplateView):
	template_name = 'quiz/create-choice.html'
