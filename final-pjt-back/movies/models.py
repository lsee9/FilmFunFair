from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=100, null=True, blank=True)
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    vote_average = models.FloatField()
    popularity = models.IntegerField()
    genres = models.CharField(max_length=100)

    def __str__(self):
        return self.title
