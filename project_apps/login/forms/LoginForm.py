from django import forms

from ..models import CustomUser
from ..validators import credentials_are_incorrect


class LoginForm(forms.ModelForm):
	email = forms.EmailField(validators=[credentials_are_incorrect])

	class Meta:
		model = CustomUser
		fields = ['email', 'password']
		widgets = {
			'password': forms.PasswordInput()
		}