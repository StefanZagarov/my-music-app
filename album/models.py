from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from user.models import User


class Album(models.Model):
    class Genre(models.TextChoices):
        POP = "Pop"
        JAZZ = "Jazz"
        RNB = "R&B"
        METAL = "Metal"
        COUNTRY = "Country"
        DANCE = "Dance"
        HIP_HOP = "Hip Hop"
        OTHER = "Other"

    album_name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=Genre.choices)
    description = models.TextField(blank=True)
    image = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    # ForeignKey is Django's Many-To-One relation
    owner = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        # Need to save the first time in order to create the pk to be used in the slug - generally unneeded since the album name is unique, but just for practice we use it
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.album_name}-{self.pk}")
            # Efficiently update only the slug field, no need to rewrite everything
            super().save(update_fields=["slug"])
