from django.urls import path

from .views.HomePageView import HomePageView
from .views.CreateRoomView import CreateRoomView
from .views.JoinRoomView import JoinRoomView
from .views.RedirectToUpdateStudentDataOrJoinRoomView import RedirectToUpdateStudentDataOrJoinRoomView
from .views.UpdateStudentIdAndCourseView import UpdateStudentIdAndCourseView
from .views.TestListView import TestListView
from .views.CreateTestView import CreateTestView
from .views.CreateQuestionView import CreateQuestionView
from .views.QuestionListView import QuestionListView
from .views.ChoiceListView import ChoiceListView

app_name = 'quiz'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create-room/', CreateRoomView.as_view(), name='create-room'),
	path('join-room/', JoinRoomView.as_view(), name='join-room'),
	path('check-data/',RedirectToUpdateStudentDataOrJoinRoomView.as_view(), name='check-data'),
	path('fill-user-data/<str:pk>', UpdateStudentIdAndCourseView.as_view(), name='fill-student-data'),
	path('display-created-tests/<int:room_id>/', TestListView.as_view(), name='test-list'),
	path('display-create-new-test/<int:pk>', CreateTestView.as_view(), name='create-test'),
	path('display-created-questions/<int:room_id>/<int:pk>', QuestionListView.as_view(), name='question-list'),
	path('display-choices/<int:room_id>/<int:test_id>/<int:question_id>', ChoiceListView.as_view(), name='choice-list'),
	path('create-question/<int:room_id>/<int:pk>', CreateQuestionView.as_view(), name='create-question'),
]