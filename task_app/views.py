from django.shortcuts import render

# Create your views here.
def home(request):
    request.session["entries_auth"] = False
    request.session["dash_auth"] = False
    return render(request, "task_app/index.html")