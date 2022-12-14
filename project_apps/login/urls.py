from django.urls import path

from .views.LandingPageView import LandingPageView
from .views.CreateAccountView import CreateAccountView
from .views.LoginView import LoginView
from .views.LogoutView import LogoutView

app_name = 'login'

urlpatterns = [
	path('', LandingPageView.as_view(), name='landing'),
	path('create-account/', CreateAccountView.as_view(), name='create-account'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout')
]