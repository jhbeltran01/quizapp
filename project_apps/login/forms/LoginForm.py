from django import forms

from ..models import Student
from ..validators import credentials_are_incorrect


class LoginForm(forms.ModelForm):
	email = forms.EmailField(validators=[credentials_are_incorrect])

	class Meta:
		model = Student
		fields = ['email', 'password']
		widgets = {
			'password': forms.PasswordInput()
		}