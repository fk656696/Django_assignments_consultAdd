from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails
from .models import Contact
from django.contrib import messages
from .serializers import ContactSerilizer
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def hello_world(request):
    return HttpResponse("Hello, world!")

def print_hello(request):
    return HttpResponse("Hello, I am djangooo!")


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


#get all user details
#get single user details
#delete single user
#update single user
def load_template(request):
    return render(request,"Auth_app/index.html")

@csrf_exempt
def data(request):
    if request.method=="GET":
        all_data=Contact.objects.all()
        sd=ContactSerializer(all_data,many=True)
        return JsonResponse({
            "success":True,
            "Data":sd.data
        })

    if request.method=="POST":
        input_data=json.loads(request.body)
        sd=ContactSerializer(data=input_data)

        if sd.is_valid():
            sd.save()
            return JsonResponse({
                "Success":True,
                "message":"Data saved successfully"
            },status=201)

@csrf_exempt
def single_usr_data(request,pk):
    if request.method=="GET":
        try:
            user=Contact.objects.get(pk=pk)
            sd=ContactSerilizer(user)

            return JsonResponse({
                "success":True,
                "Data":sd.data
            },status=200)
        except Exception as e:
            return JsonResponse({
                "Success":True,
                "message":"Data saved successfully"
            },status=500)

    if request.method=="PUT":
        try:
            user=Contact.objects.get(pk=pk)
            input_data=json.loads(request.body)

            sd=ContactSerilizer(user,data=input_data)

            if sd.is_valid():
                sd.save()
                return JsonResponse({
                "success":True,
                "message":"Data upadted successfully"
            })
        except Exception as e:
            return JsonResponse({
                "Success":False,
                "Message":str(e)
            },status=500)
    
    if request.method=="PATCH":
        try:
            user=Contact.objects.get(pk=pk)
            input_data=json.loads(request.body)

            sd=ContactSerilizer(user,data=input_data,partial=True)

            if sd.is_valid():
                sd.save()

                return JsonResponse({
                    "success":True,
                    "message":"Partial Data updated successfully"
                },status=200)
            else:
                return JsonResponse({
                    "success":False,
                    "message":"Partial Data update failed"
                },status=401)
        except Exception as e:
            return JsonResponse({
                "success":False,
                "message":str(e)
            },status=500)

    if request.method=="DELETE":
        try:
            user=Contact.objects.get(pk=pk)
            user.delete()
            return JsonResponse({
                "success":True,
                "message": "User Data Deleted successfully"
                })
        except Exception as e:
            return JsonResponse({
                "success":False,
                "message":str(e)
            },status=500)

           