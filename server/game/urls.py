from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
        path("status/<str:room>", views.status_check, name="status_check"),
        path("submit/<str:room>", views.submit, name="submit an action"),
        path("waiting/<str:room>", views.waiting, name="waiting"),
]
