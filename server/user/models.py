from django.db import models
from django.contrib.auth.models import User
from main.models import Roles
#CONST VALUES


# Create your models here.
class UserProfile(User):

    role = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name="+", null=True)
    
