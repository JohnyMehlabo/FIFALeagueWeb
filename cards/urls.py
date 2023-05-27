from django.urls import path

from . import views

urlpatterns = [
    path("", views.cards_view, name="cards_view"),
]