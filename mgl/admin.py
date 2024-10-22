from django.contrib import admin
from mgl.models import GameList

# Register your models here.

@admin.register(GameList)
class GameListAdmin(admin.ModelAdmin):
    list_display = 'id', 'game_name', 'hours_taken', 'date_finished', 'about', 'other',
    search_fields = 'id', 'name', 'hours taken', 'date finished', 'about', 'other',
    ordering = '-id',