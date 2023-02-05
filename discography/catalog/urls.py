from rest_framework import routers
from django.urls import path, include

from .views import SingerViewSet, AlbumViewSet, SongViewSet


router = routers.DefaultRouter()

router.register("singer", SingerViewSet, basename="singer")
router.register("album", AlbumViewSet, basename="album")
router.register("song", SongViewSet, basename="song")

urlpatterns = [
    path("", include(router.urls), name="api"),
]
