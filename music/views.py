from django.shortcuts import render, get_object_or_404, get_list_or_404
from music.models import Album, Artist, Song

app_name = 'music'


def index_artist(request):
    artists = Artist.objects.all()
    return render(request, 'music/index_artists.html', {'artists': artists})


def detail_artist(request, id):
    artist = get_object_or_404(Artist, id=id)
    albums = artist.album_set.filter(artist=artist)
    return render(request, 'music/detail_artist.html', {'albums': albums, 'artist': artist})


def index_album(request):
    albums = Album.objects.all()
    return render(request, 'music/index_album.html', {'albums': albums})


def detail_album(request, id):
    album = get_object_or_404(Album, id=id)
    artist = album.artist
    songs = album.song_set.all()
    return render(request, 'music/detail_album.html', {'album': album, 'songs': songs, 'artist': artist})


def favorite(request):
    song_favorite = Song.objects.filter(is_favorite=True)

    return render(request, 'music/favorite.html', {'song_favorite': song_favorite})
