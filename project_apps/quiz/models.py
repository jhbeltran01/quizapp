from django.db import models
from project_apps.login.models import CustomUser, Student

class Room(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=0)
	members = models.ManyToManyField(Student)
	name = models.CharField(max_length=100)
	is_private = models.BooleanField(default=False)
	code = models.CharField(max_length=50, default='', unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name



class Test(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	rooms = models.ManyToManyField(Room)
	text = models.CharField(max_length=500, null=False, blank=False, verbose_name='Test Name')
	passing_percentage = models.FloatField(null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.text



class Question(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	tests = models.ManyToManyField(Test)
	text = models.CharField(max_length=500, verbose_name='Question')
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