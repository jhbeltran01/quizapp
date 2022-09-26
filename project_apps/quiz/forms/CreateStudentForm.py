from django import forms

from project_apps.login.models import Student


class CreateStudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('student_id', 'course')
		widgets = {
		'student_id': forms.TextInput(attrs={'required': 'required'}),
		'course': forms.TextInput(attrs={'required': 'required'})
		}