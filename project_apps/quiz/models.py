from django.db import models
from project_apps.login.models import Student

class Room(models.Model):
	members = models.ManyToManyField(Student)
	creator_id = models.IntegerField(default=0)
	name = models.CharField(max_length=100)
	is_private = models.BooleanField(default=False)
	room_code = models.CharField(max_length=50, default='', unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name
