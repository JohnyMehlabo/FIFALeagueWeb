from django.db import models
from django.contrib.postgres.fields import ArrayField
from django import forms

class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.
    Uses Django's Postgres ArrayField
    and a MultipleChoiceField for its formfield.
    """
class Player(models.Model):
    scored_goals = models.IntegerField(default=0)
    saves = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=15)
    assists = models.IntegerField(default=0)
    times_mvp = models.IntegerField(default=0)
    exact_positions = ArrayField(models.CharField(max_length=3), 8)
    fifa_rating = models.IntegerField(default=0)
    
class Team(models.Model):
    name = models.CharField(max_length=30)
    image_name = models.CharField(max_length=30)
    team_owner = models.CharField(max_length=15)
    players = models.ManyToManyField(Player)
