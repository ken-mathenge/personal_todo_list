"""Add todo list form."""
from django import forms

from .models import TodoList


class TodoListForm(forms.ModelForm):
    """Create a form to add list."""

    class Meta:
        """Meta class."""

        model = TodoList
        fields = ["item", "completed"]
