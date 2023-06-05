
from django.contrib.auth.models import User
from django.db import models
import threading
import time

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
    user = models.CharField(max_length=20)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"<{self.pk}: {self.user}>"
    


class Game(models.Model):
    player1 = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="+")
    player2 = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="+", null=True)

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)

    def init_the_game(self):
        self.role1 = self.player1.role
        self.init = False
        wait_thread = threading.Thread(target=self.wait_for_p2)
        wait_thread.start()
        wait_thread.join(TIME_TO_WAIT)
        if self.init:
            #TODO
            pass
        
        else:
            #TODO: Log
            self.delete()


    def role_play(self):
        #TODO
        pass

    def is_valid(self):
        #TODO
        raise NotImplementedError


    def wait_for_p2(self):
        while True:
            try:
                p2 = self.player2
                if p2.is_valid():
                    self.init = True
                    return True
            except:
                time.sleep(REFRESH_TIME_FOR_PL2)

