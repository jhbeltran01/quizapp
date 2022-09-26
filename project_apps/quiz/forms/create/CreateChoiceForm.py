from dataclasses import field
from django import forms

from ...models import Choice


class CreateChoiceForm(forms.ModelForm):
  class Meta:
    model = Choice
    fields = ('text', 'is_the_correct_answer')