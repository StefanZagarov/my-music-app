from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# @deconstructible tells Django how to write this instance into a migration file as `MinLength(2)`
# Without it, makemigrations crashes with "Cannot serialize" when this validator is used on a model field
# TL;DR: @deconstructible makes this class serializable into migration files — required for any custom validator used on a model field.
@deconstructible
class MinLength:
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value: str):
        if len(value) < self.min_length:
            raise ValidationError(
                f"Input must be at least {self.min_length} characters"
            )

    # Lets Django detect "same config" between migrations; without it, makemigrations may generate spurious no-op migrations.
    def __eq__(self, other):
        return isinstance(other, MinLength) and self.min_length == other.min_length
