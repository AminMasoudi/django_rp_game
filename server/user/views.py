from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .models import UserProfile
from django.http import JsonResponse
from main.models import Roles
# Create your views here.


def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password,)
        if user:
            login(request, user)
            return JsonResponse({
                'user' : user.get_username()
            })
    return JsonResponse({
         "username" : "", 
         "password" : ""
    })

            

#Signup Page
def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = Roles.objects.get(name=request.POST['role'])
        user = UserProfile.objects.create(username=username, password=password)
        login(request, user)
        return JsonResponse({"msg":"OK"})

    if request.method == "GET":
        roles = Roles.objects.all()
        roles = list(map(lambda role : role.rep(), roles))
        return JsonResponse({
            "msg"     : "username, password, and role_name",
            "username": "",
            "password": "",
            "roles"   : roles
        })
    

    if request.user.is_authenticated:
        logout(request)
    return JsonResponse({
         "username" : "", 
         "password" : ""
    })



def log_out(request):
    logout(request)
    return JsonResponse({
        "msg" : "OK"
    })
