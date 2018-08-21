from music.models import Album, Artist, Song
from django.views.generic import ListView, DetailView

app_name = 'music'


class IndexViewAlbum(ListView):
    model = Album
    template_name = 'music/index_album.html'
    context_object_name = 'albums'


class DetailViewAlbum(DetailView):
    model = Album
    template_name = 'music/detail_album.html'
    context_object_name = 'album'


class IndexViewArtist(ListView):
    model = Artist
    template_name = 'music/index_artist.html'
    context_object_name = 'artists'


class DetailViewArtist(DetailView):
    model = Artist
    template_name = 'music/detail_artist.html'
    context_object_name = 'artist'


class FavoriteViewSong(ListView):
    model = Song
    template_name = 'music/favorite.html'
    context_object_name = 'favorite_songs'

    def get_queryset(self):
        return Song.objects.filter(is_favorite=True)


class IndexViewSong(ListView):
    model = Song
    template_name = 'music/index_song.html'
    context_object_name = 'songs'


class DetailViewSong(DetailView):
    model = Song
    template_name = 'music/detail_song.html'
    context_object_name = 'song'
