from django.urls import path

from .views.HomePageView import HomePageView
from .views.CreateRoomView import CreateRoomView
from .views.JoinRoomView import JoinRoomView
from .views.RedirectToUpdateStudentDataOrJoinRoomView import RedirectToUpdateStudentDataOrJoinRoomView
from .views.UpdateStudentIdAndCourseView import UpdateStudentIdAndCourseView
from .views.TestListView import TestListView
from .views.CreateTestView import CreateTestView
from .views.CreateQuestionView import CreateQuestionView

app_name = 'quiz'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create-room/', CreateRoomView.as_view(), name='create-room'),
	path('join-room/', JoinRoomView.as_view(), name='join-room'),
	path('check-data/',RedirectToUpdateStudentDataOrJoinRoomView.as_view(), name='check-data'),
	path('fill-user-data/<str:pk>', UpdateStudentIdAndCourseView.as_view(), name='fill-student-data'),
	path('created-tests/<int:room_id>/', TestListView.as_view(), name='test-list'),
	path('create-new-test/<int:pk>', CreateTestView.as_view(), name='create-test'),
	path('create-question/<int:pk>', CreateQuestionView.as_view(), name='create-question'),
]