from email import message
from rest_framework import status
from rest_framework.response import Response
# function based view
# from rest_framework.decorators import api_view

#class based view
from rest_framework.views import APIView

#generic based views (mixin). Typically when using the generic views, you'll override the view, and set several class attributes.
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# One of the big wins of using class-based views is that it allows us to easily compose reusable bits of behaviour. The create/retrieve/update/delete operations that we've been using so far are going to be pretty similar for any model-backed API views we create. Those bits of common behaviour are implemented in REST framework's mixin classes.
# The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. This allows for more flexible composition of behavior.
# https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
from rest_framework import mixins


from watchlist_app.models import Review, Watchlist,StreamPlatform
from watchlist_app.api.serializers import WatchlistSerializer,StreamPlatformSerializer,ReviewSerializer

# Using Concrete View Classes
# https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-generic-class-based-views

# THIS IS NOT SHOW SPESIFIC 
# class ReviewList(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    # Save and deletion hooks: The following methods are provided by the mixin classes, and provide easy overriding of the object save or deletion behavior.
    # def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
    
    def perform_create(self,serializer):

        print(serializer)
        # GET DATA JSON FROM FORM >> data={'rating': 1, 'description': '1', 'active': False}

        # pk from parameter or form
        # pk = self.kwargs.get('pk')
        pk = self.kwargs['pk']
        # get Watchlist form
        # if you know it's one object that matches your query, use get. It will fail if it's more than one.
        # otherwise use filter, which gives you a list of objects.
        # filter similiar with .filter.all() in flask, it will return Query Set (List of Clas). <class 'django.db.models.query.QuerySet'> . <QuerySet [<Watchlist: The Mandalorian>]>.
        # Whereas .all() in django will return all list without filtering
        # get similiar with .filter.first() in flask, will return <class 'watchlist_app.models.Watchlist'> . <The Mandalorian>.
        # Because we only want to get 1 spesific class, use get instead
        movie = Watchlist.objects.get(pk=pk)
        # movie_old = Review.objects.get(watchlist=pk)

        print("pk : ",pk)
        # print("pk_old : ",pk_old)
        print("movie : ",type(movie))
        print("movie : ",movie)

        # for i in movie:
        #     print(i) 
        # <class 'watchlist_app.models.Watchlist'>
        # print("movie_old : ",movie_old)

        # then save it to watchlist ReviewSerializer which integrated with Watchlist model

        serializer.save(watchlist=movie)

        # WITH this serializer will overide created & update object


class ReviewList(generics.ListAPIView):
    # 'ReviewList' should either include a `serializer_class` attribute, or override the `get_serializer_class()` method.
    serializer_class = ReviewSerializer

    # get_queryset(self) is Method in https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview . Returns the queryset that should be used for list views, and that should be used as the base for lookups in detail views. Defaults to returning the queryset specified by the queryset attribute.

    def get_queryset(self):
        # kwarfs is to get value from ReviewList.pk
        pk = self.kwargs['pk']
        # print(self) >> <watchlist_app.api.views.ReviewList object at 0x0000021E4C4ADA00>
        # print(self.kwargs) >> {'pk': 2}
        # print(self.kwargs['pk']) >> 2
        
        # Review is from Models Review
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# '''
# # Using GenericAPIView and Mixins
# class ReviewDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     # Retrieve will get one data from spesific id, whereas list get all data (list)
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         return self.put(request, *args, **kwargs)   

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# # Using GenericAPIView and Mixins
# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)    

# '''

# USING VIEWSET & ROUTERS. THIS IS CONFUSING NOT RECOMENDED
# class StreamPlatformVS(viewsets.ViewSet):

#     # ERROR : type object 'StreamPlatform' has no attribute 'objects'. Because Class name same with Model name (StreamPlatform) so change class name to StreamPlatformVS  

#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True,context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         # `HyperlinkedRelatedField` requires the request in the serializer context. Add `context={'request': request}` when instantiating the serializer.
#         serializer = StreamPlatformSerializer(watchlist,context={'request': request})
#         return Response(serializer.data)


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
    def get(self,request,pk):

        try:
            platform = StreamPlatform.objects.get(pk=pk)
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

    def put(self,request,pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
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

    def delete(self,request,pk):
        # in DELETE doesnt need Serializer because it dont need to return json

        try :
            platform = StreamPlatform.objects.get(pk=pk)

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

    def get(self,request,pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
            # print("movie : ", movie) output will return Class of <Object1>

        except Watchlist.DoesNotExist:
            # Because will return only 1 QuerySet by id so doesnt need many=True in serializer
            # How Serializer Works? Convert Class of <Object1> in movie DB to JSON but validate first with MovieSerializer

            return Response({"message":"Movie Not Found !"},status=status.HTTP_404_NOT_FOUND)

        serializer = WatchlistSerializer(movie)

        # print("serializer : ",serializer) , ouput : MovieSerializer(<Movie: Star Wars Mandalorian>)

        return Response(serializer.data)        

    def put(self,request,pk):

        try:
            movie = Watchlist.objects.get(pk=pk)

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

    def delete(self,request,pk):

        # in DELETE doesnt need Serializer because it dont need to return json

        try :
            movie = Watchlist.objects.get(pk=pk)

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
