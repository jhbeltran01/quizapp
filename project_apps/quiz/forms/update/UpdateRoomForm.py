from django import forms
from ...models import Room


class UpdateRoomForm(forms.ModelForm):
  class Meta:
    model = Room
    fields = ('name', 'code', 'is_private')