from django.db import models
from django.utils import timezone
from account.models import User
# Create your models here.
class Todolist(models.Model):
    user_id = models.ForeignKey('account.User',on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length = 100)
    image = models.ImageField()
    description = models.TextField()
    write_time = models.DateField(default=timezone.now)
    finish_time = models.DateTimeField()

    def __str__(self):
        return str(self.title)