from django.views import generic
from project_apps.login.models import CustomUser, Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ...forms.CreateStudentForm import CreateStudentForm

class CreateStudent(LoginRequiredMixin, generic.UpdateView):
	model = CustomUser
	form_class = CreateStudentForm
	template_name = 'quiz/update-student-data.html'


	def form_valid(self, form):
		new_student = Student(user=self.request.user, student_id=form.cleaned_data['student_id'], course=form.cleaned_data['course'])
		new_student.save()
		return HttpResponseRedirect(reverse('quiz:join-room'))