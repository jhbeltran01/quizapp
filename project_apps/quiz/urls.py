from django.urls import path

from .views.HomePageView import HomePageView
from .views.CreateRoomView import CreateRoomView
from .views.JoinRoomView import JoinRoomView

app_name = 'quiz'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create-room/', CreateRoomView.as_view(), name='create-room'),
	path('join-room/', JoinRoomView.as_view(), name='join-room')
]