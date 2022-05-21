from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from apps.movies.get_movies import get_movie_set_by_page
from apps.movies.serializers import movie_set_serializer

class MovieView(APIView):
    def get(self, request, *args, **kwargs):
        page = int(self.request.GET.get("page",1))
        limit = 10
        
        movie_set = get_movie_set_by_page(page=page, limit=limit)
        
        data = [movie_set_serializer(movie=movie) for movie in movie_set]
        
        return Response(data=data, status=status.HTTP_200_OK)