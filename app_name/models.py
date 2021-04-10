from django.db import models
from django.utils.timezone import now


class ToDoItem(models.Model):
    content = models.TextField()
    created = models.DateTimeField(default=now)
    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)