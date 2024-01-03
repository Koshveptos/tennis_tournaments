from django.db import models

# Create your models here.

class athlete(models.Model):
    First_name = models.CharField(max_length=30)
    Second_name = models.CharField(max_length=30)
    Country = models.CharField(max_length=50)


    def __str__(self):
        return self.title


class game(models.Model):
    game_score = models.BooleanField()
    coaf_first = models.FloatField(default=0)
    coaf_second = models.FloatField(default=0)


    def __str__(self):
        return self.title

