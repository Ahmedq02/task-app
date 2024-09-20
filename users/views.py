# from django.contrib.auth import login, logout
# from django.shortcuts import redirect, render
# from .forms import PasskeyForm
# from .models import Passkey

# def logout_view(request):
#     logout(request)
#     return redirect("/")

# def login(request):
#     if request.method == "POST":
#         form = PasskeyForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("/")
#     else:
#         form = PasskeyForm()
#     return render(request, "users/login.html", {"form": form})


