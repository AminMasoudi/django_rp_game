from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.urls import reverse
from .helpers import del_profile
from .models import UserProfile, Rolls
# Create your views here.

def index(request):
    if request.method == "GET":
        return JsonResponse({
            "msg":"W3LC0M3",
            "init-link": reverse("main:auth"),
            })
    
def auth(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user = request.user
            logout(request)
            del_profile(user)
        rolls = Rolls.objects.all()
        rolls = list(map(lambda roll : roll.rep(), rolls))
        return JsonResponse({
            "todo"  : "auth",
            "name"  : "",
            "rolls" : rolls
        })
    
    name = request.POST['name']
    roll = request.POST['roll']
    if not UserProfile.objects.get(name=name):
        user = UserProfile.objects.create(name=name)
        user.roll = Rolls.objects.get(name=roll)
        return JsonResponse({
            'msg'   : 'DONE',
            'user'  : name,
            'roll'  : roll,
            'next'  : reverse("main:start")
        })




@login_required
def start(request):
    if request.method == "GET":
        pass