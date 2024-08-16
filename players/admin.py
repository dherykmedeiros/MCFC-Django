from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdm(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'position','idade','dominant_leg', 'specialty')

