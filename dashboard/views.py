from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display_dashboard(request):
    return render(request, "dashboard/index.html")