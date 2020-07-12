from django.db import models
from django.utils import timezone
# Create your models here.


class MyUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user_name)
