from email import message
from rest_framework import status
from rest_framework.response import Response
# function based view
# from rest_framework.decorators import api_view

#class based view
from rest_framework.views import APIView

from watchlist_app.models import Watchlist,StreamPlatform
from watchlist_app.api.serializers import WatchlistSerializer,StreamPlatformSerializer

class StreamPlatformListAV(APIView):
    def get(self,request):
        
        platforms = StreamPlatform.objects.all()
        
        print("platforms :", platforms)
        # platforms return <QuerySet [<Object1>, <Object2>,..]>,  And we are trying to serialize the list as a single object. Use many=True tells the serializer that a list of objects being passed for serialization.
        
        # How Serializer Works? Convert QuerySet in platform DB to JSON but validate first with MovieSerializer
        # ERROR : `HyperlinkedRelatedField` requires the request in the serializer context. Add `context={'request': request}` when instantiating the serializer.
        serializer = StreamPlatformSerializer(platforms, many=True , context={'request': request})

        # print("serializer :", serializer.data[1]['name']) output : "Disney"
        
        return Response(serializer.data)

    def post(self,request):

        # Get requested data from input form then Serializer it to StreamPlatformSerializer
        serializer = StreamPlatformSerializer(data=request.data)

        print("serializer : ",serializer)
        # output : StreamPlatformSerializer(data={'id': 3, 'name': 'IQIYI', 'about': 'IQIYI', 'website': 'http://www.iq.com'})

        # if valid then save to serializer & DB 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):
    def get(self,request,id):

        try:
            platform = StreamPlatform.objects.get(id=id)
            # print("platform : ", platform)
            # output will return Class of <Object1>

        except StreamPlatform.DoesNotExist:

            # Because will return only 1 QuerySet by id so doesnt need many=True in serializer
            # How Serializer Works? Convert Class of <Object1> in movie DB to JSON but validate first with StreamPlatformSerializer
            return Response({"message":"Platform Not Found !"},status=status.HTTP_404_NOT_FOUND)

        # ERROR : `HyperlinkedRelatedField` requires the request in the serializer context. Add `context={'request': request}` when instantiating the serializer.
        serializer = StreamPlatformSerializer(platform, context={'request': request})
        # print("serializer : ",serializer)
        # ouput : StreamPlatformSerializer(<StreamPlatform: Disney>)

        return Response(serializer.data)        

    def put(self,request,id):
        try:
            platform = StreamPlatform.objects.get(id=id)
        except StreamPlatform.DoesNotExist:
            return Response({"message":"Platform Not Found !"},status=status.HTTP_404_NOT_FOUND)

        # Convert and validate updated data with serializer. Then update movie DB (spesific id) with that data. Remember def update(self, instance,validated_data) ! movie is current class DB which will pass instance & data is updated data given from form / input which will pass validated_data
        serializer = StreamPlatformSerializer(platform, data=request.data)

        # print("serializer : ",serializer)
        # output : MovieSerializer(data={'name': 'Disney', 'about': 'Disney', 'website': 'http://www.disney.com'})

        #  if valid then save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # return error if format not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        # in DELETE doesnt need Serializer because it dont need to return json

        try :
            platform = StreamPlatform.objects.get(id=id)

        except StreamPlatform.DoesNotExist:

            return Response({"message":"Platform Not Found !"},status=status.HTTP_404_NOT_FOUND)

        platform.delete()

        return Response({"message":"Platform has been deleted !"})

# class based view
class WatchListAV(APIView):

    def get(self,request):

        movies = Watchlist.objects.all()

        # print("movies :", movies)
        # movies return <QuerySet [<Object1>, <Object2>,..]>,  And we are trying to serialize the list as a single object. Use many=True tells the serializer that a list of objects being passed for serialization.
        
        # How Serializer Works? Convert QuerySet in movies DB to JSON but validate first with MovieSerializer

        serializer = WatchlistSerializer(movies, many=True)

        # print("serializer :", serializer.data[1]['name']) output : Starwars Mandalorian

        return Response(serializer.data)

    def post(self,request):
        # Get requested data from input form then Serializer it to MovieSerializer

        serializer = WatchlistSerializer(data=request.data)

        # print("serializer : ",serializer) , output : MovieSerializer(data={'name': 'Mandor Harian', 'description': 'About Mandor', 'active': False})

        # if valid then save to serializer & DB 
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchDetailAV(APIView):

    def get(self,request,id):
        try:
            movie = Watchlist.objects.get(id=id)
            # print("movie : ", movie) output will return Class of <Object1>

        except Watchlist.DoesNotExist:
            # Because will return only 1 QuerySet by id so doesnt need many=True in serializer
            # How Serializer Works? Convert Class of <Object1> in movie DB to JSON but validate first with MovieSerializer

            return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)

        serializer = WatchlistSerializer(movie)

        # print("serializer : ",serializer) , ouput : MovieSerializer(<Movie: Star Wars Mandalorian>)

        return Response(serializer.data)        

    def put(self,request,id):

        try:
            movie = Watchlist.objects.get(id=id)

        except Watchlist.DoesNotExist:

            return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)

        # Convert and validate updated data with serializer. Then update movie DB (spesific id) with that data. Remember def update(self, instance,validated_data) ! movie is current class DB which will pass instance & data is updated data given from form / input which will pass validated_data

        serializer = WatchlistSerializer(movie, data=request.data)

        # print("serializer : ",serializer) , output : MovieSerializer(data={'name': 'Mandor Harian', 'description': 'About Mandor', 'active': False})
        #  if valid then save
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            # return error if format not valid

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):

        # in DELETE doesnt need Serializer because it dont need to return json

        try :
            movie = Watchlist.objects.get(id=id)

        except Watchlist.DoesNotExist:

            return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)

        movie.delete()

        return Response({"message":"Movie has been deleted !"})
























# # function based
# @api_view(["GET","POST"])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         # print("movies :", movies)
#         # movies return <QuerySet [<Object1>, <Object2>,..]>,  And we are trying to serialize the list as a single object. Use many=True tells the serializer that a list of objects being passed for serialization.
        
#         # How Serializer Works? Convert QuerySet in movies DB to JSON but validate first with MovieSerializer
#         serializer = MovieSerializer(movies, many=True)

#         # print("serializer :", serializer.data[1]['name']) output : Starwars Mandalorian
#         return Response(serializer.data)

#     if request.method == 'POST':
#         # Get requested data from input form then Serializer it to MovieSerializer
#         serializer = MovieSerializer(data=request.data)
#         # print("serializer : ",serializer) , output : MovieSerializer(data={'name': 'Mandor Harian', 'description': 'About Mandor', 'active': False})

#         # if valid then save to serializer & DB 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # DoesNotExist at /movie/1
# # Movie matching query does not exist. If parameters passed None it will be error. Example there is no id = 1

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,id):

#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(id=id)
#             # print("movie : ", movie) output will return Class of <Object1>
#         except Movie.DoesNotExist:
#             # Because will return only 1 QuerySet by id so doesnt need many=True in serializer
#             # How Serializer Works? Convert Class of <Object1> in movie DB to JSON but validate first with MovieSerializer
#             return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movie)
#         # print("serializer : ",serializer) , ouput : MovieSerializer(<Movie: Star Wars Mandalorian>)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)

#         # Convert and validate updated data with serializer. Then update movie DB (spesific id) with that data. Remember def update(self, instance,validated_data) ! movie is current class DB which will pass instance & data is updated data given from form / input which will pass validated_data
#         serializer = MovieSerializer(movie, data=request.data)

#         # print("serializer : ",serializer) , output : MovieSerializer(data={'name': 'Mandor Harian', 'description': 'About Mandor', 'active': False})
#         #  if valid then save
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             # return error if format not valid
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         # in DELETE doesnt need Serializer because it dont need to return json
#         try :
#             movie = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)
#         movie.delete()
#         return Response({"message":"Movie has been deleted !"})
