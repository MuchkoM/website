from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        mode = Artist
        fields = ['name', 'photo']
