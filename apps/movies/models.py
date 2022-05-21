from django.db import models
from utilities.models import TimeStampModel

class Movie(TimeStampModel):
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    runtime = models.PositiveIntegerField()

class Reply(TimeStampModel):
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)