from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ...models import Room
from ...forms.JoinRoomForm import JoinRoomForm


class JoinRoomView(LoginRequiredMixin, generic.CreateView):
	model = Room
	form_class = JoinRoomForm
	template_name = 'quiz/join-room.html'

	def __init__(self):
		self.is_the_room_creator = False
		self.room_exist = True


	def post(self, *args, **kwargs):
		self.object = None
		return self.form_valid(super().get_form_class())


	def form_valid(self, form):
		self.room_exist = self.check_if_room_exist()

		if not self.room_exist:
			return super().form_invalid(form)

		self.is_the_room_creator = self.check_if_user_is_room_creator()

		if self.is_the_room_creator:
			return super().form_invalid(form)
		else:
			self.join_room()
			return HttpResponseRedirect(reverse('quiz:home'))


	def check_if_room_exist(self):
		self.rooms = Room.objects.filter(code=self.request.POST['code'])
		return self.rooms.exists()


	def check_if_user_is_room_creator(self):
		self.room = self.rooms[0]
		return self.room.user.id == self.request.user.id


	def join_room(self):
		self.room.members.add(self.request.user.student)


	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['room_creator'] = 'You cannot join a room that you created!' if self.is_the_room_creator else ''
		context['room_does_not_exist'] = 'The room code doesn\'t matched any room!' if not self.room_exist else '' 

		return context