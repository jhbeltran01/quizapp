from django.db import models
from project_apps.login.models import Student
from django.core.validators import MaxValueValidator, MinValueValidator

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



class Test(models.Model):
	rooms = models.ManyToManyField(Room)
	text = models.CharField(max_length=500, null=False, blank=False, verbose_name='Test Name')
	passing_percentage = models.FloatField(null=False, blank=False)
	# publish_at = models.DateTimeField(default=timezone.now)
	# time_limit = models.IntegerField(default=0)
	# close_at = models.DateTimeField()
	# started_at = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.text



class Question(models.Model):
	tests = models.ManyToManyField(Test)
	text = models.CharField(max_length=500, verbose_name='Question')
	# correct_answer = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.text



class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.CharField(max_length=200, verbose_name="Choice")
  vote = models.IntegerField(default=0)
  is_the_correct_answer = models.BooleanField(default=False)
  
  
  def __str__(self):
    return self.text