from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.core.validators import MaxValueValidator


# Create your models here.
class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter movie genre",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("genre-detail", args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="genre_name_case_insensitive_unique",
                violation_error_message="Genre already exists (case insensitive match)",
            )
        ]


class MPAARating(models.Model):
    label = models.CharField(max_length=200)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="assets/images/")
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre, related_name="genre")
    language = models.CharField(max_length=100)
    mpaaRating = models.ForeignKey(MPAARating, on_delete=models.CASCADE, related_name="movies")
    userRating = models.IntegerField(validators=[MaxValueValidator(5, message="Maximum rating is 5")])

    def __str__(self):
        return self.name
