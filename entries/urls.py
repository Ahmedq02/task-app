from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_entries, name="entries"),
    path("add_task/", views.add_task, name="add_task"),
    path("edit_task/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
]