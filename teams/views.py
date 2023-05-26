from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Team, Player

def index(request):
    context = {
        "teams" : Team.objects.all
    }
    return render(request, "teams/teams_list.html", context)

def team_view(request, team_id):
    team = Team.objects.get(id=team_id)
    context = {
        "owner" : team.team_owner,
        "team_name" : team.name,
        "players" : team.players.all
    }

    return render(request, "teams/team.html", context)