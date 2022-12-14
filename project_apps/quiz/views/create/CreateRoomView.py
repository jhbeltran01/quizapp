from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from ...models import Room
from ...forms.create.CreateRoomForm import CreateRoomForm

class CreateRoomView(LoginRequiredMixin, generic.CreateView):
	model = Room
	form_class = CreateRoomForm
	template_name = 'quiz/create-room.html'


	def form_valid(self, form):
		new_room = self.request.user.room_set.create(
			name=form.cleaned_data['name'], 
			code=form.cleaned_data['code'], 
			is_private=form.cleaned_data['is_private'])

		new_room.save()

		return HttpResponseRedirect(reverse('quiz:test', args=(new_room.id,)))