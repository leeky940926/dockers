import json
from rest_framework.test import APITestCase, APIClient
from movies.models import Movie, Reply

class TestMovieListView(APITestCase):
    def setUp(self) :
        movie1 = Movie.objects.create(
            title = "test1",
            year = 2022,
            rating = 3.5,
            runtime = 95
        )
        movie2 = Movie.objects.create(
            title = "test2",
            year = 2022,
            rating = 6.5,
            runtime = 100
        )
        movie3 = Movie.objects.create(
            title = "test3",
            year = 2022,
            rating = 2.4,
            runtime = 120
        )
        movie4 = Movie.objects.create(
            title = "test4",
            year = 2022,
            rating = 9.4,
            runtime = 80
        )
        movie5 = Movie.objects.create(
            title = "test5",
            year = 2022,
            rating = 7.5,
            runtime = 75
        )
        movie6 = Movie.objects.create(
            title = "test6",
            year = 2022,
            rating = 6.6,
            runtime = 95
        )
        reply1 = Reply.objects.create(
            movie = movie1,
            title = "reply1",
            content = "재미있어요",
            rating = 5
        )
        reply2 = Reply.objects.create(
            movie = movie2,
            title = "reply2",
            content = "흐이로워요",
            rating = 5
        )
        reply3 = Reply.objects.create(
            movie = movie3,
            title = "reply3",
            content = "그저그래여",
            rating = 5
        )
        
    def tearDown(self) :
        Reply.objects.all().delete()
        Movie.objects.all().delete()
        
    client = APIClient()
    
    def test_movie_list_view(self):
        url = "/api/movies/"
        response = self.client.get(path=url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(),
            [
                {
                    "movie_id" : 1,
                    "movie_title" : "test1",
                    "movie_rating" : 3.5,
                    "movie_runtime" : 95,
                    "movie_replies" : [
                        {
                            "reply_id" : 1,
                            "reply_title" : "reply1",
                            "reply_content" : "재미있어요",
                            "reply_rating" : 5
                        }
                    ]
                },
                {
                    "movie_id" : 2,
                    "movie_title" : "test2",
                    "movie_rating" : 6.5,
                    "movie_runtime" : 100,
                    "movie_replies" : [
                        {
                            "reply_id" : 2,
                            "reply_title" : "reply2",
                            "reply_content" : "흐이로워요",
                            "reply_rating" : 5
                        }
                    ]
                },
                {
                    "movie_id" : 3,
                    "movie_title" : "test3",
                    "movie_rating" : 2.4,
                    "movie_runtime" : 120,
                    "movie_replies" : [
                        {
                            "reply_id" : 3,
                            "reply_title" : "reply3",
                            "reply_content" : "그저그래여",
                            "reply_rating" : 5
                        }
                    ]
                },
                {
                    "movie_id" : 4,
                    "movie_title" : "test4",
                    "movie_rating" : 9.4,
                    "movie_runtime" : 80,
                    "movie_replies" : []
                },
                {
                    "movie_id" : 5,
                    "movie_title" : "test5",
                    "movie_rating" : 7.5,
                    "movie_runtime" : 75,
                    "movie_replies" : []
                }
            ]
        )
    
    def test_movie_create(self):
        url = "/api/movies/"
        
        request_body = {
            "title" : "unit test movies",
            "year" : 2022,
            "rating" : 7.8,
            "runtime" : 120,
            "background_image" : "www.image.com"
        }
        
        response = self.client.post(path=url, data=json.dumps(request_body), content_type="application/json")
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.json(),{"message":"생성되었습니다."})
    
    def test_movie_create_null_constraints(self):
        url = "/api/movies/"
        
        request_body = {
            "year" : 2022,
            "rating" : 7.8,
            "runtime" : 120,
            "background_image" : "www.image.com"
        }
        
        response = self.client.post(path=url, data=json.dumps(request_body), content_type="application/json")
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.json(), {"message":"전부 입력했는지 확인해주세요!"})
        