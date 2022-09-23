from django.views import generic

from ..models import Question

class QuestionListView(generic.ListView):
	model = Question
	template_name = 'quiz/question-list.html'
	context_object_name = 'questions_list'


	def get(self, request, *args, **kwargs):
		self.room_id = kwargs['room_id']
		self.test_id = kwargs['pk']
		return super().get(request, *args, **kwargs)


	def get_queryset(self):
		return self.request.user.room_set.get(pk=self.room_id).test_set.get(pk=self.test_id).question_set.all()


	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['room_id'] = self.room_id
		context['test_id'] = self.test_id
		return context