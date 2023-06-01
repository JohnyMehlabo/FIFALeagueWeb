from django.db import models
from django.contrib.postgres.fields import ArrayField
from django import forms

class Player(models.Model):
    scored_goals = models.IntegerField(default=0)
    saves = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=15)
    assists = models.IntegerField(default=0)
    times_mvp = models.IntegerField(default=0)
    exact_positions = ArrayField(models.CharField(max_length=3), 8)
    fifa_rating = models.IntegerField(default=0)

class MarketPlayer(Player):
    nacionality = models.CharField(max_length=20)
    foot = models.CharField(max_length=10)
    weight = models.IntegerField()
    height = models.FloatField()
    image = models.CharField(max_length=40)

    speed_stat_min = models.IntegerField()
    dribbling_stat_min = models.IntegerField()
    shooting_stat_min = models.IntegerField()
    passing_stat_min = models.IntegerField()
    physical_stat_min = models.IntegerField()
    defense_stat_min = models.IntegerField()
    tackle_stat_min = models.IntegerField()
    steal_stat_min = models.IntegerField()
    speed_stat_max = models.IntegerField()
    dribbling_stat_max = models.IntegerField()
    shooting_stat_max = models.IntegerField()
    passing_stat_max = models.IntegerField()
    physical_stat_max = models.IntegerField()
    defense_stat_max = models.IntegerField()
    tackle_stat_max = models.IntegerField()
    steal_stat_max = models.IntegerField()
    

class MarketKeeper(MarketPlayer):
    speed_stat_min = None
    dribbling_stat_min = None
    shooting_stat_min = None
    passing_stat_min = None
    physical_stat_min = None
    defense_stat_min = None
    tackle_stat_min = None
    steal_stat_min = None
    speed_stat_max = None
    dribbling_stat_max = None
    shooting_stat_max = None
    passing_stat_max = None
    physical_stat_max = None
    defense_stat_max = None
    tackle_stat_max = None
    steal_stat_max = None

    e_stat_min = models.IntegerField()
    r_stat_min = models.IntegerField()
    pa_stat_min = models.IntegerField()
    s_stat_min = models.IntegerField()
    po_stat_min = models.IntegerField()
    v_stat_min = models.IntegerField()
    e_stat_max = models.IntegerField()
    r_stat_max = models.IntegerField()
    pa_stat_max = models.IntegerField()
    s_stat_max = models.IntegerField()
    po_stat_max = models.IntegerField()
    v_stat_max = models.IntegerField()

class Team(models.Model):
    name = models.CharField(max_length=30)
    image_name = models.CharField(max_length=30)
    team_owner = models.CharField(max_length=15)
    players = models.ManyToManyField(Player)
