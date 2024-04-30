from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class MPAARating(models.Model):
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre, related_name="movies")
    language = models.CharField(max_length=100)
    mpaaRating = models.ForeignKey(
        MPAARating, on_delete=models.CASCADE, related_name="movies"
    )
    userRating = models.CharField(max_length=10)

    def __str__(self):
        return self.name
