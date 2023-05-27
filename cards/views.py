from django.shortcuts import render
from .models import Card

def cards_view(request):
    cards = Card.objects.all()

    context = {
        "cards" : cards
    }

    return render(request, "cards/cards.html", context)