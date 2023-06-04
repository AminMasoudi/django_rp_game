
from django.contrib.auth.models import User
from django.db import models


class Rolls(models.Model):
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
    user = models.CharField(max_length=20)
    roll = models.ForeignKey(Rolls, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"<{self.pk}: {self.user}>"
    


class Game(models.Model):
    player1 = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="+")
    player2 = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="+", null=True)

    roll_of_1 = models.ForeignKey(Rolls,on_delete=models.CASCADE, related_name="+")
    roll_of_2 = models.ForeignKey(Rolls, on_delete=models.CASCADE, related_name="+", null=True)

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
