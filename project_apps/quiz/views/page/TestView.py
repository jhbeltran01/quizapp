from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from ...forms.create.CreateTestForm import CreateTestForm
from ...models import Test


class TestView(LoginRequiredMixin, generic.ListView, generic.CreateView):
	model = Test
	template_name = 'quiz/test.html'
	form_class = CreateTestForm
	context_object_name = 'test_list'

	def get(self, *args, **kwargs):
		self.object = None
		self.set_needed_ids(**kwargs)
		return super().get(*args, **kwargs)


	def post(self, request, *args, **kwargs):
		self.set_needed_ids(**kwargs)
		return super().post(request, *args, **kwargs)


	def form_valid(self, form):
		room = self.request.user.room_set.get(pk=self.room_id)
		new_test = self.request.user.test_set.create(text=form.cleaned_data['text'], passing_percentage=form.cleaned_data['passing_percentage'])
		new_test.rooms.add(room)
		return HttpResponseRedirect(reverse('quiz:question', args=(self.room_id, new_test.id)))


	def get_queryset(self):
		return self.request.user.room_set.get(pk=self.room_id).test_set.all()


	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['room_id'] = self.room_id
		return context


	def set_needed_ids(self, **kwargs):
		self.room_id = kwargs['room_id']