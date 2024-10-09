from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def display_dashboard(request):
    return render(request, "dashboard/index.html")
