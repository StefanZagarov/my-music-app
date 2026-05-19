from django.shortcuts import render

from album.models import Album
from user.forms import UserForm
from user.models import User


def home_page(request):
    user = User.objects.first()
    albums = Album.objects.all()

    context = {"user": user, "albums": albums}
    form_context = {"form": UserForm()}

    if user:
        return render(
            request, template_name="common/home-with-profile.html", context=context
        )

    return render(
        request, template_name="common/home-no-profile.html", context=form_context
    )
