from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import MoviePetition, Vote
from .forms import PetitionForm


def index(request):
    """Displays a list of all active movie petitions, ordered by vote count."""

    template_data = {}
    template_data['title'] = 'Movie Petitions'

    # Annotate petitions with the total number of votes and order by the count
    petitions = MoviePetition.objects.annotate(
        vote_count=Count('votes')
    ).order_by('-vote_count', 'created_at')

    # Check if the current user has voted on each petition (for UI)
    if request.user.is_authenticated:
        voted_petitions = request.user.vote_set.values_list('petition__id', flat=True)
        for petition in petitions:
            petition.has_voted = petition.id in voted_petitions

    template_data['petitions'] = petitions

    return render(request, 'petitions/index.html', {'template_data': template_data})


@login_required
def new_petition(request):
    """Handles the creation of a new movie petition."""
    template_data = {'title': 'Start New Petition'}

    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.posted_by = request.user
            petition.save()
            return redirect('petitions:index')
    else:
        form = PetitionForm()

    template_data['form'] = form
    return render(request, 'petitions/new_petition.html', {'template_data': template_data})


@login_required
def vote(request, petition_id):
    """Handles a user voting on a specific petition."""
    petition = get_object_or_404(MoviePetition, pk=petition_id)

    # Check if the user has already voted
    if not Vote.objects.filter(petition=petition, user=request.user).exists():
        # Create the vote
        Vote.objects.create(petition=petition, user=request.user)

    # Redirect back to the petitions list
    return redirect('petitions:index')