from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Team, Player
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def index(request):
    context = {
        "teams" : Team.objects.all
    }
    return render(request, "teams/teams_list.html", context)

def team_view(request, team_id):
    team = Team.objects.get(id=team_id)
    context = {
        "image_name"  :  team.image_name,
        "owner" : team.team_owner,
        "team_name" : team.name,
        "defenders" : team.players.filter(position="Defensa"),
        "atackers" : team.players.filter(position="Atacante"),
        "midfielders" : team.players.filter(position="Mediocentro"),
        "goalkeepers" : team.players.filter(position="Portero")
    }

    return render(request, "teams/team.html", context)

def player_view(request, player_id):
    player = Player.objects.get(id=player_id)
    context = {
        "player" : player
    }
    return render(request, "teams/player.html", context)

@login_required
def update_with_game_view(request):
    if request.user.is_superuser:
        if request.method == "GET":
            context = {
                "players" : Player.objects.all().order_by("name")
            }
            return render(request, "teams/add_game.html", context)
        else:
            params = [item for item in request.POST.items()][1:]
            for key,value in params:
                player = Player.objects.get(name=value)
                if key == "mvp":
                    player.times_mvp = player.times_mvp + 1
                    player.save()
                else:
                    job = key.split("-")[2]
                    if job == "keeper":
                        if player.saves != None:
                            player.saves = player.saves + 1
                        else:
                            player.saves = 1
                        player.save()
                    elif job == "scorer":
                        player.scored_goals = player.scored_goals + 1
                        player.save()
                    elif job == "assister":
                        if value != "Ninguno":
                            player.assists = player.assists + 1
                            player.save()

            return redirect("/")