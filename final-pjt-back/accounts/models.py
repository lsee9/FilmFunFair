from communities.models import Post
from django.db import models
from django.contrib.auth.models import AbstractUser
from reviews.models import Review
from movies.models import Movie
from communities.models import Post

# Create your models here.
class User(AbstractUser):
    like_review = models.ManyToManyField(Review, related_name='review_liked_user')
    like_movie = models.ManyToManyField(Movie, related_name='movie_liked_user')
    watch_movie = models.ManyToManyField(Movie, related_name='movie_watched_user')
    like_post = models.ManyToManyField(Post, related_name='post_liked_user')