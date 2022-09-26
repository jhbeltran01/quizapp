from django.urls import path

from .views.HomePageView import HomePageView
from .views.CreateRoomView import CreateRoomView
from .views.JoinRoomView import JoinRoomView
from .views.RedirectToFillStudentDataOrJoinRoomView import RedirectToFillStudentDataOrJoinRoomView
from .views.CreateStudent import CreateStudent
from .views.TestView import TestView
from .views.QuestionView import QuestionView
from .views.ChoiceView import ChoiceView
from .views.UpdateRoomView import UpdateRoomView
from .views.DeleteRoom import DeleteRoom

app_name = 'quiz'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create-room/', CreateRoomView.as_view(), name='create-room'),
	path('join-room/', JoinRoomView.as_view(), name='join-room'),
	path('check-data/',RedirectToFillStudentDataOrJoinRoomView.as_view(), name='check-data'),
	path('fill-user-data/<str:pk>', CreateStudent.as_view(), name='fill-student-data'),
	path('tests/<int:room_id>/', TestView.as_view(), name='test'),
	path('questions/<int:room_id>/<int:test_id>', QuestionView.as_view(), name='question'),
	path('choice/<int:room_id>/<int:test_id>/<int:question_id>', ChoiceView.as_view(), name='choice'),
	path('edit-room/<int:pk>', UpdateRoomView.as_view(), name='edit-room'),
	path('delete-room/<int:room_id>', DeleteRoom.as_view(), name='delete-room')
]