# --- petitions/urls.py (Verification) ---
from django.urls import path
from . import views

# This is critical for the 'petitions.index' naming
app_name = 'petitions'

urlpatterns = [
    # This line defines the name 'index' within the 'petitions' namespace
    path('', views.index, name='index'),
    path('new/', views.new_petition, name='new_petition'),
    path('<int:petition_id>/vote/', views.vote, name='vote'),
]