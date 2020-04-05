"""Todolists app url conf."""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="list"),
    path("/detail/<int:pk>/", views.TodoListDetailView.as_view(), name="detail"),
    path("/delete/<int:pk>/", views.TodoListDeleteView.as_view(), name="delete"),
    path("/create/", views.TodoListCreateView.as_view(), name="create"),
]
