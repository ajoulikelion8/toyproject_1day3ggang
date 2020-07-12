# Generated by Django 3.0.5 on 2020-07-12 16:01

import content.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[content.models.min_length_1_validator])),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(validators=[content.models.min_length_1_validator])),
                ('write_time', models.DateField(default=django.utils.timezone.now)),
                ('finish_time', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.MyUser')),
            ],
        ),
    ]