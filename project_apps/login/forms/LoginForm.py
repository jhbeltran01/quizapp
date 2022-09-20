from django import forms

from ..models import Student

class LoginForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('email', 'password')