from django import forms
from ..models import Room


class CreateRoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = ('name', 'room_code', 'is_private')