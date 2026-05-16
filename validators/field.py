from django.core.exceptions import ValidationError


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
