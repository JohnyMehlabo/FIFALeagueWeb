from django.contrib.postgres.fields import ArrayField
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=30)
    
class Team(models.Model):
    name = models.CharField(max_length=20)
    team_owner = models.CharField(max_length=15)
    players = models.ManyToManyField(Player)