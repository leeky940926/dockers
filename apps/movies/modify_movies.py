from movies.models import Movie

def create_movie(params: dict):
    
    Movie.objects.create(
        title = params["title"],
        year = params["year"],
        rating = params["rating"],
        runtime = params["runtime"],
        background_image = params["background_image"]
    )
    