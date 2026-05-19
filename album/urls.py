from django.urls import path

from album import views

urlpatterns = [
    path("add", views.add, name="album-add"),
    path("<slug:album_slug>/details", views.details, name="album-details"),
    path("<slug:album_slug>/edit", views.edit, name="album-edit"),
    path("<slug:album_slug>/delete", views.delete, name="album-delete"),
]
