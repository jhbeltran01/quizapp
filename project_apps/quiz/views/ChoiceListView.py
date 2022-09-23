from django.views import generic
from ..models import Choice


class ChoiceListView(generic.ListView):
  model = Choice
  template_name = 'quiz/list-choice.html'
  context_object_name = 'choice_list'
  
  def get(self, request, *args, **kwargs):
    self.room_id = kwargs['room_id']
    self.test_id = kwargs['test_id']
    self.question_id = kwargs['question_id']
    return super().get(request, *args, **kwargs)
  
    """
      Returns the choices of the selected question
    """
  def get_queryset(self, *args, **kwargs):
    return self.request.user.room_set.get(pk=self.room_id).test_set.get(pk=self.test_id).question_set.get(pk=self.question_id).choice_set.all()