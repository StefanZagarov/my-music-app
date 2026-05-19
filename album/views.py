from django.shortcuts import redirect, render

from album.forms import AlbumForm
from album.models import Album
from user.models import User


def add(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        # We don;t want to commit to saving it yet since we still have to add the owner (editable=False, so it's not in the form), commit=False returns the unsaved Album instance, then we attach the owner and after that we save it
        print("FORM IS VALID, SAVING...")
        album = form.save(commit=False)
        album.owner = User.objects.first()
        print("OWNER:", album.owner)
        album.save()
        print(f"SAVED ALBUM: {album.pk}, SLUG: {album.slug}")
        return redirect("home")
    # This carries errors for failed POSTs
    print(f"FORM INVALID. Errors: {form.errors.as_json()}")
    return render(request, "album/album-add.html", {"form": form})


def details(request, album_slug):
    album = Album.objects.get(slug=album_slug)

    context = {"album": album}
    return render(request, template_name="album/album-details.html", context=context)


def edit(request, album_slug):
    album = Album.objects.get(slug=album_slug)
    # The whole magic of prefilling the form happens here at `instance=album` - Django uses instance to pre-fill the form fields with the album's data
    form = AlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        # On POST submit the form is bout to request.POST, but since we have instance=album that tells Django "this is an update, not a create", so when form.save() runs, it does an UPDATE on the existing row (SQL item)
        form.save()
        return redirect("album-details", album_slug=album.slug)

    return render(request, "album/album-edit.html", {"form": form})


def delete(request, album_slug):
    album = Album.objects.get(slug=album_slug)
    form = AlbumForm(request.POST or None, instance=album)
    # Make form fields readonly
    for field in form.fields.values():
        field.disabled = True

    if request.method == "POST":
        album.delete()
        return redirect("home")

    return render(request, "album/album-delete.html", {"form": form})
