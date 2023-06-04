from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path("", views.index, name="homepage"),
    path("auth/", views.auth, name="auth"),
    path("start/", views.start, name="start"),

]
