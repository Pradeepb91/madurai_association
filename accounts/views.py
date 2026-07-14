from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def admin_login(request):
    if request.user.is_authenticated:
        return redirect("portal_dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("portal_dashboard")

        messages.error(
            request,
            "Invalid Username or Password."
        )

    return render(request, "admin_login.html")

from django.contrib.auth import logout


def admin_logout(request):
    logout(request)
    return redirect("home")
