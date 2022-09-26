from django.views import generic
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login

from ..models import CustomUser
from ..forms.CreateAccountForm import CreateAccountForm


class CreateAccountView(generic.CreateView):
	model = CustomUser
	form_class = CreateAccountForm
	template_name = 'login/create-account.html'
	success_url = '/'

	def form_valid(self, form):
		new_user = CustomUser(
			username=form.cleaned_data['username'],
			email=form.cleaned_data['email'],
			password=make_password(form.cleaned_data['password'], salt='pbkdf2_sha256'),
			first_name=form.cleaned_data['first_name'],
			last_name=form.cleaned_data['last_name'],
			middle_name=form.cleaned_data['middle_name'])
		
		new_user.save()
		login(self.request, new_user)

		return HttpResponseRedirect(reverse('quiz:home')) 