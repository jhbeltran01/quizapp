# Generated by Django 4.1.1 on 2022-09-20 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_room_user_remove_room_creator_id_room_creator_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='creator_id',
            field=models.IntegerField(default=0),
        ),
    ]
