# Generated by Django 2.1.1 on 2020-07-09 04:43

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(validators=[content.models.min_length_1_validator]),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=100, validators=[content.models.min_length_1_validator]),
        ),
    ]