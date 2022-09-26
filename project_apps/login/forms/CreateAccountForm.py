from django import forms

from ..models import CustomUser

class CreateAccountForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'password', 'first_name', 'last_name', 'middle_name']

		widgets = {
			'username': forms.TextInput(attrs={'placeholder': 'Username'}),
			'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
			'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
			'student_id': forms.TextInput(attrs={'class': 'hidden'}),
			'course': forms.TextInput(attrs={'class': 'hidden'}),
			'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
			'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
			'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
		}