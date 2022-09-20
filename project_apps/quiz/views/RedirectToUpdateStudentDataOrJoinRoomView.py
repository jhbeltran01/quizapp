from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

class RedirectToUpdateStudentDataOrJoinRoomView(generic.RedirectView):
	def get(self, *args, **kwargs):
		print(self.request.user.student_id)
		if self.request.user.student_id is None or self.request.user.course is None:
			return HttpResponseRedirect(reverse('quiz:fill-student-data', args=('1',)))
		else:
			return HttpResponseRedirect(reverse('quiz:join-room'))