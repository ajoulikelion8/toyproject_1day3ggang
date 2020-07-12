from django import forms
from django.db import models
from django.utils import timezone
from account.models import MyUser
# Create your models here.

# 한글자 이상 쓰지 않으면 오류가 나게 하는 함수


def min_length_1_validator(value):
    if len(value) < 1:
        raise forms.ValidationError('1글자 이상 입력해주세요')


class Todolist(models.Model):
    user_id = models.ForeignKey(
        'account.MyUser', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, validators=[
                             min_length_1_validator])
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(validators=[min_length_1_validator])
    write_time = models.DateField(default=timezone.now)
    finish_time = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.title)

    def summary(self):
        return self.description[:100]
