from django.urls import path

from .views.HomePageView import HomePageView
from .views.CreateRoomView import CreateRoomView
from .views.JoinRoomView import JoinRoomView
from .views.RedirectToUpdateStudentDataOrJoinRoomView import RedirectToUpdateStudentDataOrJoinRoomView
from .views.UpdateStudentIdAndCourseView import UpdateStudentIdAndCourseView
from .views.TestView import TestView
from .views.QuestionView import QuestionView
from .views.ChoiceView import ChoiceView

app_name = 'quiz'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create-room/', CreateRoomView.as_view(), name='create-room'),
	path('join-room/', JoinRoomView.as_view(), name='join-room'),
	path('check-data/',RedirectToUpdateStudentDataOrJoinRoomView.as_view(), name='check-data'),
	path('fill-user-data/<str:pk>', UpdateStudentIdAndCourseView.as_view(), name='fill-student-data'),
	path('tests/<int:room_id>/', TestView.as_view(), name='test'),
	path('questions/<int:room_id>/<int:pk>', QuestionView.as_view(), name='question'),
	path('choice/<int:room_id>/<int:test_id>/<int:question_id>', ChoiceView.as_view(), name='choice')
]