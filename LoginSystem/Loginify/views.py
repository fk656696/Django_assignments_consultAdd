from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails
from django.contrib import messages

# Create your views here.


# def hello_world(request):
#     return HttpResponse("Hello, world!")

def home(request):
    return HttpResponse("Welcome to Loginify!")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if UserDetails.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:
            UserDetails.objects.create(
                username=username, email=email, password=password
            )
            messages.success(request, "Signup successful!")
            return redirect("login")
    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = UserDetails.objects.get(username=username, password=password)
            messages.success(request, f"Welcome {user.username}!")
            return redirect("home")  # Or wherever you want
        except UserDetails.DoesNotExist:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")



