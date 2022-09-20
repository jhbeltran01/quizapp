from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

from ..models import Room
from ..forms.CreateRoomForm import CreateRoomForm

class CreateRoomView(generic.CreateView):
	model = Room
	form_class = CreateRoomForm
	template_name = 'quiz/create-room.html'


	def form_valid(self, form):
		new_room = self.request.user.room_set.create(
			name=form.cleaned_data['name'], 
			room_code=form.cleaned_data['room_code'], 
			is_private=form.cleaned_data['is_private'],
			creator_id=self.request.user.id)

		new_room.save()

		return HttpResponseRedirect(reverse('quiz:home'))