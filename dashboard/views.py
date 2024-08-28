from datetime import datetime, timedelta
import json
from django.shortcuts import render
from django.http import HttpResponse
from entries.models import Task

# Create your views here.
def display_dashboard(request):
    today = datetime.today()
    next_30_days = today + timedelta(days=30)

    tasks = Task.objects.filter(due_by__range=[today, next_30_days])

    line_labels = []
    line_data = []

    for i in range(31):
        day = today + timedelta(days=i)
        line_labels.append(day.strftime('%Y-%m-%d'))
        day_task_count = tasks.filter(due_by__date=day).count()
        line_data.append(day_task_count)
    
    pie_labels = ["Low", "Medium", "High"]
    pie_data = []

    for i in range(1,4):
        count = Task.objects.filter(priority=i).count()
        pie_data.append(count)
    
    context = {
        "line_labels": json.dumps(line_labels),
        "line_data": json.dumps(line_data),
        "pie_labels": json.dumps(pie_labels),
        "pie_data": json.dumps(pie_data),
    }

    return render(request, "dashboard/index.html", context)