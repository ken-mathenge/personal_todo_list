"""Todo list models."""
from django.db import models


class TodoList(models.Model):
    """Create list related fields."""

    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
