from django.contrib import admin
from .models import Team, Player, MarketKeeper, MarketPlayer


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(MarketPlayer)
admin.site.register(MarketKeeper)

# Register your models here.
