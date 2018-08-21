"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'music'

url_artist = [
    path('', views.index_artist, name='index_artist'),
    path('<int:id>', views.detail_artist, name='detail_artist'),
]

url_album = [
    path('', views.index_album, name='index_album'),
    path('<int:id>', views.detail_album, name='detail_album'),
]

urlpatterns = [
    path('', include(url_album)),
    path('album/', include(url_album)),
    path('artist/', include(url_artist)),
    path('favorite/', views.favorite, name='favorite'),
]
