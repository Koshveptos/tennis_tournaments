from django.db import models
from games.models import*

from django.contrib.auth.models import AbstractUser
# Create your models here.

class user(AbstractUser):
    balance = models.PositiveIntegerField(default=0,null=True,blank=True)



class basket(models.Model):
    prise_bid = models.FloatField(default=0)
    coaf_bid = models.FloatField(default=0)
    game_id = models.ForeignKey(to=game, on_delete=models.CASCADE)
    user_if = models.ForeignKey(to=user, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class sessions(models.Model):
    start_time_sessions = models.DateTimeField()
    end_time_sessions = models.DateTimeField()
    user_id = models.ForeignKey(to=user, on_delete=models.CASCADE)
    def __str__(self):
        return self.title