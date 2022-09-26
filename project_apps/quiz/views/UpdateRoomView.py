from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Room
from ..forms.EditRoomForm import EditRoomForm


class UpdateRoomView(LoginRequiredMixin, generic.UpdateView):
  model = Room
  form_class = EditRoomForm
  template_name = 'quiz/edit-room.html'
  
  def get(self, *args, **kwargs):
    self.set_needed_ids(**kwargs)
    return super().get(*args, **kwargs)
  
  
  def post(self, request, *args, **kwargs):
    self.set_needed_ids(**kwargs)
    return super().post(request, *args, **kwargs)
  
  def get_object(self, query=None):
    self.room = self.request.user.room_set.get(pk=self.room_id)
    return self.room
  
  
  def form_valid(self, form):
    form.save()
    return HttpResponseRedirect(reverse('quiz:home'))
  
  
  def set_needed_ids(self, **kwargs):
    self.room_id = kwargs['pk']