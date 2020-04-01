from django.db import models


class TodoList(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
