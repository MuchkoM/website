from music.models import Album, Artist, Song
from django.views.generic import ListView, DetailView, FormView, RedirectView
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse


app_name = 'music'


def add_artist(request):
    if request.POST:
        return HttpResponseRedirect(reverse('music:add-artist'))
    else:
        return render(request, 'music/add_artist.html')


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
