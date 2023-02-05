from django.db import models

class Singer(models.Model):
    name = models.CharField("Исполнитель", max_length=256)

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    singer_name = models.ForeignKey(Singer, verbose_name="Исполнитель", related_name="album_name", on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField("Год выпуска")

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return f"Альбом {self.id} исполнителя {self.singer_name}"


class Song(models.Model):
    title = models.CharField("Название", max_length=256)
    number = models.ManyToManyField(Album, verbose_name="Номер альбома")

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self):
        return f"{self.title}"

