from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from apps.movies.modify_movies import create_movie
from movies.get_movies import get_movie_object_by_movie_id, get_movie_set_by_page
from movies.serializers import movie_set_serializer
from dockers.urls.docs import (
    response_movie_list_schema_dict, 
    response_movie_detail_schema_dict
)
from django.db import transaction, IntegrityError


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

'''
Swagger에 추가 안 한 POST, UPDATE, DELETE는 Swagger 데코레이터 설정 안 했을 시,
Swagger는 정말로 업데이트가 안 되는지 테스트
'''
class MovieCreateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                params = {
                    "title" : self.request.data.get("title"),
                    "year" : self.request.data.get("year"),
                    "rating" : self.request.data.get("rating"),
                    "runtime" : self.request.data.get("runtime"),
                    "background_image" : self.request.data.get("background_image")
                }
                
                create_movie(params=params)
        
        except IntegrityError:
            return Response(data={"message":"전부 입력했는지 확인해주세요!"}, status=400)
        
        else:
            return Response(data={"message":"생성되었습니다."}, status=201)
                