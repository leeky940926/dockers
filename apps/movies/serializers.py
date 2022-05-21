from movies.models import Reply
from movies.models import Movie

def movie_set_serializer(movie: Movie) -> dict:
    result = dict()
    
    result["movie_id"] = movie.id
    result["title"] = movie.title
    result["rating"] = movie.rating
    result["runtime"] = movie.runtime
    result["replies"] = [reply_set_serializer(reply=reply) for reply in movie.reply_prefetch_set]
    
    return result

def reply_set_serializer(reply: Reply) -> dict:
    result = dict()
    
    result["reply_id"] = reply.id
    result["title"] = reply.title
    result["content"] = reply.content
    result["rating"] = reply.rating
    
    return result