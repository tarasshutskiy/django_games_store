from django.contrib import admin
from .models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'poster', 'price', 'draft']
    search_fields = ['name', 'year']


@admin.register(GameScreenshot)
class GameScreenshotAdmin(admin.ModelAdmin):
    list_display = ['game_name', ]
    search_fields = ['game_name', ]


