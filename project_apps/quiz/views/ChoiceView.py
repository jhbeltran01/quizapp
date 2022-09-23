from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..forms.CreateChoiceForm import CreateChoiceForm
from ..models import Choice


class ChoiceView(LoginRequiredMixin, generic.ListView, generic.CreateView):
  model = Choice
  form_class = CreateChoiceForm
  template_name = 'quiz/choice.html'
  context_object_name = 'choice_list'
  
  def get(self, request, *args, **kwargs):
    self.object = None
    self.room_id = kwargs['room_id']
    self.test_id = kwargs['test_id']
    self.question_id = kwargs['question_id']
    return super().get(request, *args, **kwargs)
  
  
  def post(self, request, *args, **kwargs):
    self.room_id = kwargs['room_id']
    self.test_id = kwargs['test_id']
    self.question_id = kwargs['question_id']
    return super().post(request, *args, **kwargs)
  
  
  def form_valid(self, form):
    self.request.user.room_set.get(pk=self.room_id).test_set.get(pk=self.test_id).question_set.get(pk=self.question_id).choice_set.create(text=form.cleaned_data['text'], is_the_correct_answer=form.cleaned_data['is_the_correct_answer'])
    return HttpResponseRedirect(reverse('quiz:choice', args=(self.room_id, self.test_id, self.question_id)))
  
  
  """
    Returns the choices of the selected question
  """
  def get_queryset(self, *args, **kwargs):
    return self.request.user.room_set.get(pk=self.room_id).test_set.get(pk=self.test_id).question_set.get(pk=self.question_id).choice_set.all()
  
  