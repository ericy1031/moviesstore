# --- petitions/forms.py ---
from django import forms
from .models import MoviePetition

class PetitionForm(forms.ModelForm):
    class Meta:
        model = MoviePetition
        fields = ['movie_title', 'description']
        widgets = {
            'movie_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Movie Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Why should this movie be added?', 'rows': 3}),
        }