from django.views import generic
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..models import Student
from ..forms.CreateAccountForm import CreateAccountForm


class CreateAccountView(generic.CreateView):
	model = Student
	form_class = CreateAccountForm
	template_name = 'login/create-account.html'
	success_url = '/'

	def form_valid(self, form):
		new_user = Student(
			username=form.cleaned_data['username'],
			email=form.cleaned_data['email'],
			password=make_password(form.cleaned_data['password'], salt='pbkdf2_sha256'),
			first_name=form.cleaned_data['first_name'],
			last_name=form.cleaned_data['last_name'],
			middle_name=form.cleaned_data['middle_name'],
			student_id=form.cleaned_data['student_id'],
			course=form.cleaned_data['course'])
		
		new_user.save()
		return HttpResponseRedirect(reverse('login:landing')) 