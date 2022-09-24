from django import forms
from ..models import Room


class EditRoomForm(forms.ModelForm):
  class Meta:
    model = Room
    fields = ('name', 'room_code', 'is_private')