from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:team_id>/", views.team_view),
    path("player/<int:player_id>/", views.player_view),
    path("add_game", views.update_with_game_view)
]