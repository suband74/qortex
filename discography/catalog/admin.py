from django.contrib import admin

from .models import Singer, Album, Song

@admin.register(Singer)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Album)
class LettersGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "singer_name", "year")

@admin.register(Song)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "title")