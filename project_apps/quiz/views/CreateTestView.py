from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Test
from ..forms.CreateTestForm import CreateTestForm

class CreateTestView(LoginRequiredMixin, generic.CreateView):
	model = Test
	form_class = CreateTestForm
	template_name = 'quiz/create-test.html'


	def post(self, request, *args, **kwargs):
		self.room_id = kwargs['pk']
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):
		new_test = form.save()
		return HttpResponseRedirect(reverse('quiz:create-choice', args=(new_test.id,)))