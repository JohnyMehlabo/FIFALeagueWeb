from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Team, Player, MarketPlayer, MarketKeeper
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
def player_exchange(request):
    if request.user.is_superuser:
        if request.method == "GET":
            context = {
                "players" : Player.objects.all().order_by("name")
            }
            return render(request, "teams/exchange_players.html", context)
        else:
            player_1 = Player.objects.get(name=request.POST["player-1"])
            player_2 = Player.objects.get(name=request.POST["player-2"])

            team_1 = player_1.team_set.all()[0]
            team_2 = player_2.team_set.all()[0]

            player_1.team_set.set([team_2])
            player_2.team_set.set([team_1])

            player_1.save()
            player_2.save()
            return redirect("/")
            

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
                if value != "Ninguno":
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

def market_view(request):
    context = {
        "players" : [MarketPlayer.objects.get(id=161),  
                     MarketPlayer.objects.get(id=124),
                     MarketPlayer.objects.get(id=136),
                     MarketPlayer.objects.get(id=185)],
        "keepers" : [MarketKeeper.objects.get(id=151)],
        "super_star" : Player.objects.get(name="Nico Schloterbeck")
    }
    return render(request, "teams/market.html", context)