from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from validators.field import MinLength


class User(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            # Learning re-implementation of Django's MinLengthValidator — demonstrates the configurable-callable pattern via __call__.
            MinLength(2),
            RegexValidator(
                regex=r"^[A-Za-z0-9_]+$",
                message="Ensure this value contains only letters, numbers, and underscore.",
            ),
        ],
    )
    email = models.EmailField(unique=True)
    # For optional integer field use both blank and null since it can't be empty string ("") when empty, so its set to NULL
    age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
