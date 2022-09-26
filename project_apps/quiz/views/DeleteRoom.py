from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class DeleteRoom(LoginRequiredMixin, generic.DeleteView):
  def get(self, request, *args, **kwargs):
    request.user.room_set.get(pk=kwargs['room_id']).delete()
    return HttpResponseRedirect(reverse('quiz:home'))