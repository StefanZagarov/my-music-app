from django import forms

from album.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["album_name", "artist", "genre", "description", "image", "price"]
        labels = {
            "album_name": "Album Name",
            "artist": "Artist",
            "genre": "Genre",
            "description": "Description",
            "image": "Image URL",
            "price": "Price",
        }
        widgets = {
            "album_name": forms.TextInput(attrs={"placeholder": "Album Name"}),
            "artist": forms.TextInput(attrs={"placeholder": "Artist"}),
            "description": forms.Textarea(attrs={"placeholder": "Description"}),
            "image": forms.URLInput(attrs={"placeholder": "Image URL"}),
            "price": forms.NumberInput(attrs={"placeholder": "Price"}),
        }
        error_messages = {"album_name": {"unique": "This album name already exists"}}
