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
        "defenders" : team.players.filter(position="Defensa"),
        "atackers" : team.players.filter(position="Atacante"),
        "midfielders" : team.players.filter(position="Mediocentro"),
        "goalkeepers" : team.players.filter(position="Portero")
    }

    return render(request, "teams/team.html", context)