from movies.models import Reply
from movies.models import Movie

def movie_set_serializer(movie: Movie) -> dict:
    result = dict()
    
    result["movie_id"] = movie.id
    result["movie_title"] = movie.title
    result["movie_rating"] = movie.rating
    result["movie_runtime"] = movie.runtime
    result["movie_replies"] = [reply_set_serializer(reply=reply) for reply in movie.reply_prefetch_set]
    
    return result

def reply_set_serializer(reply: Reply) -> dict:
    result = dict()
    
    result["reply_id"] = reply.id
    result["reply_title"] = reply.title
    result["reply_content"] = reply.content
    result["reply_rating"] = reply.rating
    
    return result