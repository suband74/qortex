from rest_framework.viewsets import ModelViewSet

from .models import Singer, Album, Song
from .serializers import SingerSrlz, AlbumSrlz, SongSrlz


class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSrlz


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSrlz


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSrlz
