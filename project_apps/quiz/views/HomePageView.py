from django.views import generic
from ..models import Room

class HomePageView(generic.ListView):
	model = Room
	template_name = 'quiz/home.html'
	context_object_name = 'rooms_list'


	def get_context_data(self, *args, **kwargs):
		context = {
			'joined_room_list': self.request.user.room_set.all().exclude(creator_id=self.request.user.id),
			'created_room_list': self.request.user.room_set.filter(creator_id=self.request.user.id),
		}
		return context