from django.views import generic
from project_apps.login.models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms.UpdateStudentIdAndCourseForm import UpdateStudentIdAndCourseForm

class UpdateStudentIdAndCourseView(LoginRequiredMixin, generic.UpdateView):
	model = Student
	form_class = UpdateStudentIdAndCourseForm
	template_name = 'quiz/update-student-data.html'


	def form_valid(self, form):
		self.request.user.student_id = form.cleaned_data['student_id']
		self.request.user.course = form.cleaned_data['course']
		self.request.user.save()

		return HttpResponseRedirect(reverse('quiz:join-room'))