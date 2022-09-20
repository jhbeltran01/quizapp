from django import forms

from ..models import Room


class JoinRoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = ('room_code',)