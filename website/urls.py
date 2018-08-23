from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='music')),
    path('music/', include('music.urls')),
    path('admin/', admin.site.urls),
    path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),
]
