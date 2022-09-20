from django.views import generic
from ..models import Student

class LoginView(generic.FormView):
	model = Student
	template_name = 'login/login.html'
	

	def form_valid(self, form):
		print(form)
