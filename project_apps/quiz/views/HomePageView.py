from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Room

class HomePageView(LoginRequiredMixin, generic.ListView):
	model = Room
	template_name = 'quiz/home.html'
	context_object_name = 'rooms_list'


	def get_context_data(self, *args, **kwargs):
		context = {
			'created_room_list': self.request.user.room_set.all(),
			'joined_room_list': self.request.user.student.room_set.all() if hasattr(self.request.user, 'student') else ''
		}
		return context