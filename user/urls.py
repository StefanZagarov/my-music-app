from django.urls import path

from user import views

urlpatterns = [
    path("profile/register", views.register, name="profile-register"),
    path("profile/details", views.details, name="profile-details"),
    path("profile/delete", views.delete, name="profile-delete"),
]
