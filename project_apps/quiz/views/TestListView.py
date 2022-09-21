from django.views import generic

from ..models import Test


class TestListView(generic.ListView):
	model = Test
	template_name = 'quiz/test-list.html'
	context_object_name = 'test_list'