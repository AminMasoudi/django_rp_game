from django.shortcuts import render
from django.http import JsonResponse,Http404
from .models import Game, STANDARD_ACTIONS
from django.contrib.auth.decorators import login_required
from .helpers import profile_finder



# Create your views here.
@login_required
def status_check(request, room):
    if request.method == "GET":
        code = request.GET["code"]
        game = Game.objects.get(name=room, code=code)
        if game:
            return JsonResponse({
                "status" : game.status
            })
        return Http404()


@login_required
def submit(request, room):
    if request.method == "POST":
        game = Game.objects.get(name=room, code=request.POST['code'])
        if game:
            user = profile_finder(request)
            if user == game.player1 and game.status == 'waiting':
                if user.POST['action'] in STANDARD_ACTIONS : game.p1_move = user.POST['action']
            if user == game.player2 and game.status == 'waiting':
                if user.POST['action'] in STANDARD_ACTIONS : game.p2_move = user.POST['action']
        return JsonResponse({'msg':'got it'})