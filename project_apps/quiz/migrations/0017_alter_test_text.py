# Generated by Django 4.1.1 on 2022-09-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='text',
            field=models.CharField(max_length=500, verbose_name='Test Name'),
        ),
    ]
