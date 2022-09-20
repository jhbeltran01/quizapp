from django.contrib.auth import logout
from django.views import generic

class LogoutView(generic.RedirectView):
	url = '/login/'


	def get(self, *args, **kwargs):
		logout(self.request)
		return super().get(*args, **kwargs)