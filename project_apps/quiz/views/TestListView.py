from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Test


class TestListView(LoginRequiredMixin, generic.ListView):
	model = Test
	template_name = 'quiz/test-list.html'
	context_object_name = 'test_list'

	def get(self, *args, **kwargs):
		self.room_id = kwargs['room_id']
		return super().get(*args, **kwargs)


	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['room_id'] = self.room_id
		return context