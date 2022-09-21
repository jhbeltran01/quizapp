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
	success_url = ''

	def post(self, request, *args, **kwargs):
		self.room_id = kwargs['pk']
		return super().post(request, *args, **kwargs)


	def form_valid(self, form):
		room = self.request.user.room_set.get(pk=self.room_id)
		room.test_set.create(text=form.cleaned_data['text'], passing_percentage=form.cleaned_data['passing_percentage'])
		return HttpResponseRedirect(reverse('quiz:home'))