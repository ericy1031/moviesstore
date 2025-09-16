from django.contrib import admin

from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    list_display = ('id','name', 'price', 'stock',)
    list_editable = ('stock',)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
