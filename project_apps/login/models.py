from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _


class Student(AbstractUser):
	username = models.CharField(unique=False, max_length=50)
	email = models.EmailField(_('Email'), unique=True, blank=False, null=False)
	student_id = models.CharField(max_length=20, null=True, blank=True)
	course = models.CharField(max_length=20, null=True, blank=True)
	first_name = models.CharField(max_length=200, null=False, blank=False)
	last_name = models.CharField(max_length=200, null=False, blank=False)
	middle_name = models.CharField(max_length=200, null=True, blank=True, default='')
	modified_at = models.DateTimeField(auto_now=True)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'last_name', 'first_name']


	def __str__(self):
		return self.username