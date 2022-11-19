from django.urls import path, include

urlpatterns = [
    path("movies/", include("movies.urls")),
    path("accounts/", include("accounts.urls")),
]