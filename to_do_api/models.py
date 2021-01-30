from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('task'), ('date'),)
        
    def __str__(self):
        return self.task