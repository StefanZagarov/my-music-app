from django.shortcuts import redirect, render

from user.forms import UserForm
from user.models import User


def register(request):
    #  - When someone first visits /user/profile/register/ (a GET), request.POST is empty, the form is "invalid", and the function falls through and returns None — Django will throw ValueError: didn't return an HttpResponse.
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "common/home-no-profile.html", {"form": form})


def details(request):
    # Since we do not study user authentication and authorization in Django Basics, we create only one entry for a user in the database, and we take it with .first()
    user = User.objects.first()
    if not user:
        return redirect("home")

    # <model_name_lowercase>_set - Django automatically creates a reverse relation (album.owner gives the user from the album, this is the forward relation, user.album_set gives us the albums from the user, this is the reverse)
    albums_count = user.album_set.count()
    # Alternate way to send arguments to the render
    return render(
        request,
        "user/profile-details.html",
        {"user": user, "albums_count": albums_count},
    )


def delete(request):
    user = User.objects.first()
    if not user:
        return redirect("home")
    if request.method == "POST":
        user.delete()
        return redirect("home")
    return render(request, "user/profile-delete.html")
