from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import TaskForm
from .models import Task

# Create your views here.
def display_entries(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }

    return render(request, "entries/index.html", context)

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

    
    context = {"form": form}
    return render(request, "entries/add_task.html", context)

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/entries/")
    else:
        form = TaskForm(instance=task)

    context = {"form": form}
    return render(request, "entries/edit_task.html", context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("/entries/")