from django.db.models import QuerySet, Prefetch
from movies.models import Movie, Reply

def get_movie_set_by_page(page: int, limit: int) -> QuerySet:
    movie_set = Movie.objects.prefetch_related(
        Prefetch(
            "reply_set",
            queryset=Reply.objects.all(),
            to_attr="reply_prefetch_set"
        )
    ).all()[(page-1)*limit:limit]
    return movie_set