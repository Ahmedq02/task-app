from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task


@login_required
def display_entries(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}

    return render(request, "entries/index.html", context)


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/entries/")
        else:
            print("invalid form")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }
    return render(request, "entries/add_task.html", context)


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/entries/")
    else:
        form = TaskForm(instance=task)

    context = {
        "form": form,
    }
    return render(request, "entries/edit_task.html", context)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("/entries/")
