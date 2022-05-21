from django.urls import path

from apps.movies.views import MovieView

urlpatterns = [
    path("", MovieView.as_view())
]
