from django.contrib import admin
from music.models import Album, Artist, Song
# Register your models here.


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)