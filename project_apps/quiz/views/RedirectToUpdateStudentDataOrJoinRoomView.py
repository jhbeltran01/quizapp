from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist


class RedirectToUpdateStudentDataOrJoinRoomView(LoginRequiredMixin, generic.RedirectView):
	def get(self, *args, **kwargs):
		if hasattr(self.request.user, 'student'):
			return HttpResponseRedirect(reverse('quiz:join-room'))
		else:
			return HttpResponseRedirect(reverse('quiz:fill-student-data', args=('1',)))