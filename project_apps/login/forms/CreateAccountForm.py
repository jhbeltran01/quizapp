from django import forms

from ..models import Student

class CreateAccountForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['username', 'email', 'password', 'first_name', 'last_name', 'middle_name', 'student_id', 'course']
		help_texts = {
			'student_id': '<sup>*optional</sup>',
			'course': '<sup>*optional</sup>'
		}

		widgets = {
			'username': forms.TextInput(attrs={'placeholder': 'Username'}),
			'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
			'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
			'student_id': forms.TextInput(attrs={'class': 'hidden'}),
			'course': forms.TextInput(attrs={'class': 'hidden'}),
			'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
			'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
			'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
			'student_id': forms.TextInput(attrs={'placeholder': 'Student Id'}),
			'course': forms.TextInput(attrs={'placeholder': 'Course'})
		}