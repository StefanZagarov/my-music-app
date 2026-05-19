from django import forms

from user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "age"]
        labels = {
            "username": "Your username",
            "email": "Email address",
            "age": "Age (optional)",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "age": forms.NumberInput(
                attrs={"min": 0, "max": 120, "placeholder": "Age"}
            ),
        }
        help_texts = {"username": "Letters, numbers and underscore only"}
        error_messages = {
            "username": {"unique": "That username has already been taken"}
        }
