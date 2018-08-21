from django.db import models


# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50)
    photo = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    logo = models.CharField(max_length=256)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
