from django.db import models


# Create your models here.
class Task(models.Model):
    PRIORITY = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    ]

    user_email = models.EmailField(max_length=100)
    task = models.CharField(max_length=100)
    due_by = models.DateTimeField()
    priority = models.IntegerField(choices=PRIORITY, default=1)
    is_urgent = models.BooleanField()

    class Meta:
        ordering = ["due_by"]
