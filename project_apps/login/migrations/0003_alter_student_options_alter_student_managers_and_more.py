# Generated by Django 4.1.1 on 2022-09-20 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_student_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_permissions',
        ),
    ]