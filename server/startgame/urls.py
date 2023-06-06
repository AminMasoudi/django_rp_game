from django.urls import path
from . import views


app_name = "startgame"


urlpatterns = [
    path("join/", views.join, name="join_game"),
    path("create/", views.create, name="create_game"),
]