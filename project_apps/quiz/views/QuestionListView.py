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
		print(self.room_id, self.test_id)
		return self.request.user.room_set.get(pk=self.room_id).test_set.get(pk=self.test_id).question_set.all()