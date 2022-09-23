from django import forms

from ..models import Test


class CreateTestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = ('text', 'passing_percentage')
		widgets = {
			'passing_percentage': forms.NumberInput(attrs={'min': 1, 'max': 100})
		}