from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..models import Test
from ..forms.CreateTestForm import CreateTestForm

class CreateTestView(generic.CreateView):
	model = Test
	form_class = CreateTestForm
	template_name = 'quiz/create-test.html'


	def post(self, request, *args, **kwargs):
		self.room_id = kwargs['pk']
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):
		new_test = self.request.user.room_set.get(pk=self.room_id).test_set.create(text=form.cleaned_data['text'], passing_percentage=form.cleaned_data['passing_percentage'])
		new_test.save()
		return HttpResponseRedirect(reverse('quiz:create-choice', args=(new_test.id,)))