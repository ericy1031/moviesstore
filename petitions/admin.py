# --- petitions/admin.py ---
from django.contrib import admin
from .models import MoviePetition, Vote

admin.site.register(MoviePetition)
admin.site.register(Vote)