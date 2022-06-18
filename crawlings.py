import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dockers.settings')

django.setup()
import requests

from faker import Faker
from django.db import transaction
from apps.movies.models import Movie, Reply

f = Faker()

#Movie Crawling
with transaction.atomic():
    for page in range(1,5):
        try:
            params = {
                "page" :page,
                "limit" : 20
            }
            responses = requests.get(url="https://yts.torrentbay.to/api/v2/list_movies.json", params=params).json()["data"]["movies"]
            
            for response in responses:
                movie = Movie.objects.create(
                    title=response["title"], 
                    year=response["year"],
                    rating=response["rating"],
                    runtime=response["runtime"],
                    background_image=response["background_image_original"]
                )
                
                for _ in range(10):
                    Reply.objects.create(
                        movie_id=movie.id,
                        title=f.text(),
                        content=f.text(),
                        rating=f.pyint(min_value=0, max_value=10)*0.6
                    )
        
        except KeyError:
            continue

