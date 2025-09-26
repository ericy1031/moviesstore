from django.db import models
from django.contrib.auth.models import User


class MoviePetition(models.Model):
    """Represents a request by a user to add a movie to the catalog."""

    # The title of the movie being petitioned
    movie_title = models.CharField(max_length=255, unique=True)

    # User who originally posted the petition
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='petitions')

    # Date the petition was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Optional: A brief reason/description for the movie
    description = models.TextField(blank=True, null=True)

    def total_votes(self):
        """Returns the total number of votes for this petition."""
        return self.votes.count()

    def __str__(self):
        return f'Petition for: {self.movie_title}'


class Vote(models.Model):
    """Represents a single user's vote for a petition."""

    # The petition being voted on
    petition = models.ForeignKey(MoviePetition, on_delete=models.CASCADE, related_name='votes')

    # The user who cast the vote
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Date the vote was cast
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user can only vote once per petition
        unique_together = ('petition', 'user')

    def __str__(self):
        return f'{self.user.username} voted on {self.petition.movie_title}'
