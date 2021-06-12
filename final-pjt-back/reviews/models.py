from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_review')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')
    star = models.FloatField()
    oneline_comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

