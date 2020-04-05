"""Todolists app views."""
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

# from django.contrib import messages
# from django.shortcuts import redirect, render

# from .forms import TodoListForm
from .models import TodoList


class TodoListView(ListView):
    """Todo list list view."""

    model = TodoList
    template_name = "home.html"
    context_object_name = "lists"


class TodoListDetailView(DetailView):
    """Todo list detail view."""

    model = TodoList
    template_name = "details.html"
    context_object_name = "details"


class TodoListCreateView(CreateView):
    """Add an item to a todo list."""

    model = TodoList
    fields = ["item", "details", "remind_on"]
    template_name = "create.html"


class TodoListDeleteView(DeleteView):
    """Delete an item from the list."""

    model = TodoList
    success_url = reverse_lazy("list")
