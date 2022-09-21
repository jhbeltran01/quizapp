from django.views import generic

class CreateChoiceView(generic.TemplateView):
	template_name = 'quiz/create-choice.html'
