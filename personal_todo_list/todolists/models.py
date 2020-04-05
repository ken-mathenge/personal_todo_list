"""Todo list models."""
from django.db import models


class TodoList(models.Model):
    """Create list related fields."""

    item = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    details = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    remind_on = models.DateTimeField()

    def __str__(self):
        """Item human readable form."""
        return f"{self.item} : {self.completed}"
