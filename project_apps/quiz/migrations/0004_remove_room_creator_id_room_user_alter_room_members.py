# Generated by Django 4.1.1 on 2022-09-26 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0001_initial'),
        ('quiz', '0003_alter_question_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='creator_id',
        ),
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(to='login.student'),
        ),
    ]
