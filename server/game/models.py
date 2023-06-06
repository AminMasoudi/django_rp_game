from django.db import models
from main.models import Roles
from user.models import UserProfile
import time
import threading




REFRESH_TIME_FOR_PL2 = 1
TIME_TO_WAIT = 300

STANDARD_ACTIONS = ["def",
                    "shot",
                    "fight",
                    ]

GAME_STATUS = [
    "pending",
    "waiting",
    "new_result"
]

# Create your models here.

class Game(models.Model):
    player1 = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="+")
    player2 = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="+", null=True)

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)

    def init_the_game(self):
        self.role1 = self.player1.role
        self.init = False
        self.status = GAME_STATUS[0]
        wait_thread = threading.Thread(target=self.wait_for_p2)
        wait_thread.start()
        wait_thread.join(TIME_TO_WAIT)
        if self.init:
            self.status = GAME_STATUS[1]

        else:
            #TODO: Log
            self.delete()


    def role_play(self):
        #TODO
        return NotImplementedError

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

