from django.db import models

# Create your models here.
class Task(models.Model):
    user_email = models.EmailField(max_length=100)
    task = models.CharField(max_length=100)
    due_by = models.DateTimeField()
    priority = models.IntegerField()
    is_urgent = models.BooleanField()