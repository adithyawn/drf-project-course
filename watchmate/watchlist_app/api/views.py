from email import message
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view(["GET","POST"])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        # print("movies :", movies)
        # movies return <QuerySet [<Object1>, <Object2>,..]>,  And we are trying to serialize the list as a single object. Use many=True tells the serializer that a list of objects being passed for serialization.
        
        # How Serializer Works? Convert QuerySet in movies DB to JSON but validate first with MovieSerializer
        serializer = MovieSerializer(movies, many=True)

        # print("serializer :", serializer.data[1]['name']) output : Starwars Mandalorian
        return Response(serializer.data)

    if request.method == 'POST':
        # Get requested data from input form then Serializer it to MovieSerializer
        serializer = MovieSerializer(data=request.data)
        # print("serializer : ",serializer) , output : MovieSerializer(data={'name': 'Mandor Harian', 'description': 'About Mandor', 'active': False})

        # if valid then save to serializer & DB 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DoesNotExist at /movie/1
# Movie matching query does not exist. If parameters passed None it will be error. Example there is no id = 1

@api_view(['GET','PUT','DELETE'])
def movie_details(request,id):

    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=id)
            # print("movie : ", movie) output will return Class of <Object1>
        except Movie.DoesNotExist:
            # Because will return only 1 QuerySet by id so doesnt need many=True in serializer
            # How Serializer Works? Convert Class of <Object1> in movie DB to JSON but validate first with MovieSerializer
            return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        # print("serializer : ",serializer) , ouput : MovieSerializer(<Movie: Star Wars Mandalorian>)
        return Response(serializer.data)

    if request.method == 'PUT':
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)

        # Convert and validate updated data with serializer. Then update movie DB (spesific id) with that data. Remember def update(self, instance,validated_data) ! movie is current class DB which will pass instance & data is updated data given from form / input which will pass validated_data
        serializer = MovieSerializer(movie, data=request.data)

        # print("serializer : ",serializer) , output : MovieSerializer(data={'name': 'Mandor Harian', 'description': 'About Mandor', 'active': False})
        #  if valid then save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # return error if format not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        # in DELETE doesnt need Serializer because it dont need to return json
        try :
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({"message":"Movie has been deleted !"})
