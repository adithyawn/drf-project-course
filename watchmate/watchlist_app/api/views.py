from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    # print("movies :", movies)
    # movies return <QuerySet [<Object1>, <Object2>,..]>,  And we are trying to serialize the list as a single object. Use many=True tells the serializer that a list of objects being passed for serialization.
    serializer = MovieSerializer(movies, many=True)
    # print("serializer :", serializer.data[1]['name']) output : Starwars Mandalorian

    return Response(serializer.data)

# DoesNotExist at /movie/1
# Movie matching query does not exist. If parameters passed None it will be error. Example there is no id = 1

@api_view()
def movie_details(request,id):
    movie = Movie.objects.get(id=id)
    # Because will return only 1 QuerySet by id so doesnt need many=True
    serializer = MovieSerializer(movie)
    # print("serializer :", serializer.data['name']) output : Starwars Mandalorian

    return Response(serializer.data)