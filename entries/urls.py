from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_entries, name="entries"),
    path("add/", views.add_task, name="add_task"),
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
