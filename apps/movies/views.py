from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from apps.movies.get_movies import get_movie_object_by_movie_id, get_movie_set_by_page
from apps.movies.serializers import movie_set_serializer
from dockers.urls.docs import response_movie_list_schema_dict, response_movie_detail_schema_dict


class MovieListView(APIView):
    @swagger_auto_schema(responses=response_movie_list_schema_dict)
    def get(self, request, *args, **kwargs):
        page = int(self.request.GET.get("page",1))
        limit = 5
        
        movie_set = get_movie_set_by_page(page=page, limit=limit)
        
        data = [movie_set_serializer(movie=movie) for movie in movie_set]
        
        return Response(data=data, status=status.HTTP_200_OK)

class MovieDetailView(APIView):
    @swagger_auto_schema(responses=response_movie_detail_schema_dict)
    def get(self, request, *args, **kwargs):
        movie_id = self.kwargs.get("movie_id")
        
        movie = get_movie_object_by_movie_id(movie_id=movie_id)
        
        if not movie:
            return Response(data={"message" : "영화ID를 확인해주세요"}, status=status.HTTP_404_NOT_FOUND)
        
        data = movie_set_serializer(movie=movie)
        
        return Response(data=data, status=status.HTTP_200_OK)
