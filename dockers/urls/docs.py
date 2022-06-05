from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="기획부터 배포까지!",
      default_version='v1',
      description='''기획부터 배포까지 프로젝트의 영화 API에 대한 문서입니다. 
      각 API에서 Try it out을 통해 서버 내 존재하는 영화 데이터를 직접 확인하실 수 있습니다!
      만약, 내부 코드에 대해 더 알고 싶으시다면, 아래 Terms of service를 눌러주세요!
      Git Repository로 이동합니다!
      문의 및 수정사항 필요 시, 아래 Contact the developer를 눌러서 이메일 부탁드립니다!''',
      terms_of_service="https://github.com/leeky940926/dockers",
      contact=openapi.Contact(email="leeky940926@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

response_movie_list_schema_dict = {
    "200": openapi.Response(
        description="데이터 조회에 성공했습니다."
    )
}

response_movie_detail_schema_dict = {
    "200": openapi.Response(
        description="데이터 조회에 성공했습니다."
    ),
    "404": openapi.Response(
        description="영화가 존재하지 않습니다."
    )
}

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]