"""Todolists app views."""
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import TodoListForm
from .models import TodoList


def home(request):
    """View to add a post."""
    if request.method == "POST":
        form = TodoListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = TodoList.objects.all
            messages.success(request, ("Item successfully added"))
            return render(request, "home.html", {"all_items": all_items})

    else:
        all_items = TodoList.objects.all
        return render(request, "home.html", {"all_items": all_items})


def delete(request, list_id):
    """View to delete a post."""
    item = TodoList.objects.get(pk=list_id)
    item.delete()
    return redirect("home")
