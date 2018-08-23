from django.urls import path, include
from .views import (DetailViewArtist, DetailViewAlbum, FavoriteViewSong, IndexViewArtist,
                    IndexViewAlbum, IndexViewSong, add_artist, DetailViewSong)
from django.views.generic import RedirectView

app_name = 'music'

url_artist = [
    path('', IndexViewArtist.as_view(), name='index_artist'),
    path('<int:pk>', DetailViewArtist.as_view(), name='detail_artist'),
    path('add', add_artist, name='add-artist')
]

url_album = [
    path('', IndexViewAlbum.as_view(), name='index_album'),
    path('<int:pk>', DetailViewAlbum.as_view(), name='detail_album'),
]

url_song = [
    path('', IndexViewSong.as_view(), name='index_song'),
    path('<int:pk>', DetailViewSong.as_view(), name='detail_song'),
]

urlpatterns = [
    path('', RedirectView.as_view(url='album/')),
    path('album/', include(url_album)),
    path('artist/', include(url_artist)),
    path('song/', include(url_song)),
    path('favorite/', FavoriteViewSong.as_view(), name='favorite_song'),
]
