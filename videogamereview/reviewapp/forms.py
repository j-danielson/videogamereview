from itertools import product
from socket import fromshare
from django import forms
from .models import Videogame, Vgreview

class VideoGameForm(forms.ModelForm):
    class Meta:
        model=Videogame
        fields='__all__'
        labels = {
            'ReleaseDate' : 'Release Date'
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Vgreview
        fields='__all__'