from datetime import datetime, timedelta
import json
from django.shortcuts import render
from django.http import HttpResponse
from entries.models import Task

# Create your views here.
def display_dashboard(request):
    # authentication
    required_password = "ahm123"
    auth = request.session.get("dash_auth", False)

    if request.method == "POST":
        password = request.POST.get("password")
        if password == required_password:
            auth = True
            request.session["dash_auth"] = True

    today = datetime.today()
    next_30_days = today + timedelta(days=30)
    # get the tasks due in the next 30 days
    next_tasks = Task.objects.filter(due_by__range=[today, next_30_days])

    # create the line chart
    line_labels = []
    line_data = []

    for i in range(31):
        day = today + timedelta(days=i)
        line_labels.append(day.strftime('%Y-%m-%d'))
        day_task_count = next_tasks.filter(due_by__date=day).count()
        line_data.append(day_task_count)
    
    # create the pie chart
    pie_labels = ["Low", "Medium", "High"]
    pie_data = []

    for i in range(1,4):
        count = Task.objects.filter(priority=i).count()
        pie_data.append(count)
    
    # gets the urgent tasks that are due in the next 30 days
    urgent_tasks = next_tasks.filter(is_urgent=True).count()

    tasks = Task.objects.all()
    
    context = {
        "line_labels": json.dumps(line_labels),
        "line_data": json.dumps(line_data),
        "pie_labels": json.dumps(pie_labels),
        "pie_data": json.dumps(pie_data),
        "urgent_tasks": urgent_tasks,
        "tasks": tasks,
        "auth": auth,
    }

    return render(request, "dashboard/index.html", context)