from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from ...forms.create.CreateChoiceForm import CreateChoiceForm
from ...models import Choice


class ChoiceView(LoginRequiredMixin, generic.ListView, generic.CreateView):
  model = Choice
  form_class = CreateChoiceForm
  template_name = 'quiz/choice.html'
  context_object_name = 'choice_list'
  
  
  
  def get(self, request, *args, **kwargs):
    self.object = None
    self.set_needed_ids(**kwargs)
    self.set_question_object()
    return super().get(request, *args, **kwargs)
  
  
  
  def post(self, request, *args, **kwargs):
    self.set_needed_ids(**kwargs)
    self.set_question_object()
    return super().post(request, *args, **kwargs)
  
  
  
  """
    Create a new choice
  """
  def form_valid(self, form):
    self.question_object.choice_set.create(text=form.cleaned_data['text'], is_the_correct_answer=form.cleaned_data['is_the_correct_answer'])
    return HttpResponseRedirect(reverse('quiz:choice', args=(self.room_id, self.test_id, self.question_id)))
  
  
  
  """
    Returns the choices of the selected question
  """
  def get_queryset(self, *args, **kwargs):
    return self.question_object.choice_set.all()
  
  
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['room_id'] = self.room_id
    context['test_id'] = self.test_id
    return context
  
  
  
  def set_needed_ids(self, **kwargs):
    self.room_id = kwargs['room_id']
    self.test_id = kwargs['test_id']
    self.question_id = kwargs['question_id']
    
    
    
  def set_question_object(self):
    self.question_object = self.request.user.room_set.get(pk=self.room_id).test_set.get(pk=self.test_id).question_set.get(pk=self.question_id)