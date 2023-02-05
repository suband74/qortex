from rest_framework import serializers

from .models import Singer, Album, Song


class SingerSrlz(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"


class AlbumSrlz(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class SongSrlz(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"