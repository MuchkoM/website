from django.urls import path, include
from .views import DetailViewArtist, DetailViewAlbum, FavoriteViewSong, IndexViewArtist, IndexViewAlbum

app_name = 'music'

url_artist = [
    path('', IndexViewArtist.as_view(), name='index_artist'),
    path('<int:pk>', DetailViewArtist.as_view(), name='detail_artist'),
]

url_album = [
    path('', IndexViewAlbum.as_view(), name='index_album'),
    path('<int:pk>', DetailViewAlbum.as_view(), name='detail_album'),
]

urlpatterns = [
    path('', include(url_album)),
    path('album/', include(url_album)),
    path('artist/', include(url_artist)),
    path('favorite/', FavoriteViewSong.as_view(), name='favorite_song'),
]
