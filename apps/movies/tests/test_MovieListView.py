from rest_framework.test import APITestCase

from movies.models import Movie, Reply

class MovieListViewTest(APITestCase):
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
    
    