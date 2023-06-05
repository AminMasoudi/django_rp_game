from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.urls import reverse
from .helpers import del_profile
from .models import UserProfile, Roles, Game
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
        roles = Roles.objects.all()
        roles = list(map(lambda role : role.rep(), roles))
        return JsonResponse({
            "todo"  : "auth",
            "name"  : "",
            "roles" : roles
        })
    
    name = request.POST['name']
    role = request.POST['role']
    if not UserProfile.objects.get(name=name):
        user = UserProfile.objects.create(name=name)
        user.role = Roles.objects.get(name=role)
        return JsonResponse({
            'msg'   : 'DONE',
            'user'  : name,
            'role'  : user.role,
            'next'  : reverse("main:start")
        })

@login_required
def start(request):
    if request.method == "GET":
        return JsonResponse({
            "msg"    : "join or create a new game", 
            "join"   : False,
            "create" : False
        })
    if request.method == "POST":
        user = UserProfile.objects.get(user=request.user)
        if request.POST["join"]:
            #join
            pass
        elif request.POST['create']:
            #create
            if Game.objects.get(name=request.POST['name']):
               return JsonResponse({
                   'msg' : 'game exist'
               })
            game = Game.objects.create(
                name=request.POST['name'],
                code=request.POST['code'],
                player1= user
            )
