from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def display_entries(request):
    return render(request, "entries/index.html")


@login_required
def add_task(request):
    return render(request, "entries/edit_task.html")


@login_required
def edit_task(request, task_id):
    context = {
        "task_id": task_id,
    }
    return render(request, "entries/edit_task.html", context)


@login_required
def dashboard(request):
    return render(request, "entries/dashboard.html")
