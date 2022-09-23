from django.contrib import admin
from .models import Room, Test, Question, Choice

admin.site.register(Room)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Choice)