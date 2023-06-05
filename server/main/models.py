
from django.contrib.auth.models import User
from django.db import models

REFRESH_TIME_FOR_PL2 = 1
TIME_TO_WAIT = 300

class Roles(models.Model):
    name    = models.CharField(max_length=20,default="No name")
    power   = models.IntegerField(default=100)

    def __str__(self):
        return f"<{self.pk}: {self.name}>"

    def rep(self) -> dict:
        d = {
            "name" : self.name,
            "power": self.power,
    
        }
        return d

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"<{self.pk}: {self.user}>"