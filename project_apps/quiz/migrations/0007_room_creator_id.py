# Generated by Django 4.1.1 on 2022-09-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_rename_user_room_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='creator_id',
            field=models.IntegerField(default=0),
        ),
    ]