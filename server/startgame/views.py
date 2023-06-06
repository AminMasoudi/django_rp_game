from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from game.models import Game
# Create your views here.

@login_required
def join(request):
    if request.method == "POST":
        game_name = request.POST["game"]
        game_code = request.POST["code"]
        game = Game.objects.get(name=game_name, code=game_code)
        if game:
            game.player2 = request.user 
            game.role2 = request.user.role
            return JsonResponse({
                "msg" : "OK"
            })
        return JsonResponse({
            "msg": "permission denied"
        })
            
    if request.method == "GET":
        return JsonResponse({
            "game" : "",
            "code" : ""
        })
    
@login_required
def create(request):
    if request.method == "POST":
        game_name = request.POST['game_name']
        if not Game.objects.get(name=game_name):
            code = request.POST["code"]
            game = Game.objects.create(name=game_name,
                                       code=code,
                                       player1=request.user)
            game.init()
            return JsonResponse({
                "msg": "OK"
            })
        return JsonResponse({
            "msg" : "game exist"
        })
    if request.method == "GET":
        return JsonResponse({
            "game_name" : "" ,
            "code": ""
        })