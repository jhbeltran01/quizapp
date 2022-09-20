from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..models import Student
from ..forms.LoginForm import LoginForm

class LoginView(generic.FormView):
	model = Student
	template_name = 'login/login.html'
	form_class = LoginForm

	def post(self, *args, **kwargs):
		return self.form_valid(self.get_form())


	def form_valid(self, form):
		user = Student.objects.filter(email=self.request.POST['email'], password=make_password(self.request.POST['password'], salt='pbkdf2_sha256'))
		has_correct_credentials = len(user) > 0
		
		if has_correct_credentials:
			login(self.request, user[0])
			return HttpResponseRedirect(reverse('quiz:home')) 
		else:
			return super().form_invalid(form)
