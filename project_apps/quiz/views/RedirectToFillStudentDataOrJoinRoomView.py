from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

"""
	If the user is a student, redirect to join room page,
	else redirect to student form page
"""
class RedirectToFillStudentDataOrJoinRoomView(LoginRequiredMixin, generic.RedirectView):
	def get(self, *args, **kwargs):
		if hasattr(self.request.user, 'student'):
			return HttpResponseRedirect(reverse('quiz:join-room'))
		else:
			return HttpResponseRedirect(reverse('quiz:fill-student-data', args=('1',)))