from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return HttpResponseRedirect(reverse("home"))


def login(request):
    if request.method == "POST":
        password = request.POST["password"]
        user = authenticate(request, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(request.GET.get("next", reverse("home")))
    else:
        return render(request, "users/login.html")
