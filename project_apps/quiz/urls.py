from django.urls import path

from .views.HomePageView import HomePageView
from .views.create.CreateRoomView import CreateRoomView
from .views.JoinRoomView import JoinRoomView
from .views.redirect.RedirectToFillStudentDataOrJoinRoomView import RedirectToFillStudentDataOrJoinRoomView
from .views.create.CreateStudentView import CreateStudentView
from .views.TestView import TestView
from .views.QuestionView import QuestionView
from .views.ChoiceView import ChoiceView
from .views.update.UpdateRoomView import UpdateRoomView
from .views.delete.DeleteRoom import DeleteRoom

app_name = 'quiz'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create-room/', CreateRoomView.as_view(), name='create-room'),
	path('join-room/', JoinRoomView.as_view(), name='join-room'),
	path('check-data/',RedirectToFillStudentDataOrJoinRoomView.as_view(), name='check-data'),
	path('fill-user-data/<str:pk>', CreateStudentView.as_view(), name='fill-student-data'),
	path('tests/<int:room_id>/', TestView.as_view(), name='test'),
	path('questions/<int:room_id>/<int:test_id>', QuestionView.as_view(), name='question'),
	path('choice/<int:room_id>/<int:test_id>/<int:question_id>', ChoiceView.as_view(), name='choice'),
	path('edit-room/<int:pk>', UpdateRoomView.as_view(), name='edit-room'),
	path('delete-room/<int:room_id>', DeleteRoom.as_view(), name='delete-room')
]