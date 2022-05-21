from django.urls import path

from apps.movies.views import MovieListView, MovieDetailView

urlpatterns = [
    path("", MovieListView.as_view()),
    path("<int:movie_id>", MovieDetailView.as_view())
]
