from django.urls import path

from .views.LandingPageView import LandingPageView
from .views.CreateAccountView import CreateAccountView

app_name = 'login'
urlpatterns = [
	path('', LandingPageView.as_view(), name='landing'),
	path('create-account/', CreateAccountView.as_view(), name='create-account')
]