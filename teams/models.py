from django.db import models

class Player(models.Model):
    scored_goals = models.IntegerField(default=0)
    saves = models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=15)
    
class Team(models.Model):
    name = models.CharField(max_length=30)
    image_name = models.CharField(max_length=30)
    team_owner = models.CharField(max_length=15)
    players = models.ManyToManyField(Player)
