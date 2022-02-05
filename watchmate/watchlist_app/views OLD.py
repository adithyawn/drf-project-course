# '''
# # OLD CODE WITHOUT DRF
# from django.shortcuts import render

# # import model
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.
# # this is function based view
# def movie_list(request):
#     # get all object from db
#     movies = Movie.objects.all()

#     print(movies)
#     # output : list of object <QuerySet [<Movie: Upin Ipin Movie>, <Movie: Boboboboi Sang Penyelamat>]>

#     print(movies.values())
#     #output list of object <QuerySet [{'id': 1, 'name': 'Upin Ipin Movie', 'description': 'Kisah 2 Anak Botak', 'active': True}, {'id': 2, 'name': 'Boboboboi Sang Penyelamat', 'description': 'Kisah Adudu Menyelamatkan Dunia', 'active': False}]>

#     print(list(movies.values()))
#     # convert Query Set to List [{'id': 1, 'name': 'Upin Ipin Movie', 'description': 'Kisah 2 Anak Botak', 'active': True}, {'id': 2, 'name': 'Boboboboi Sang Penyelamat', 'description': 'Kisah Adudu Menyelamatkan Dunia', 'active': False}]

#     list_movies = list(movies.values())

#     data = {"movies": list_movies}

#     return JsonResponse(data)
#     # data : { movies : [{id: 1, name: "Upin Ipin Movie", description: "Kisah 2 Anak Botak", active: true}, {id: 2, name: "Boboboboi Sang Penyelamat", description: "Kisah Adudu Menyelamatkan Dunia", active: false}] }


# def movie_details(request,id):
#     # get class object with (id = id parameter)
#     movies = Movie.objects.get(id=id)

#     print("OUTPUT :", movies)
#     # output class object : <Upin Ipin Movie>

#     movie_id = movies.id
#     movie_name = movies.name
#     movie_desc = movies.description
#     movie_status = movies.active

#     print(movie_name)
#     # output string : Upin Ipin Movie

#     data = {
#         "id": movie_id,
#         "name":movie_name,
#         "desc":movie_desc,
#         "movie_status":movie_status
#         }

#     return JsonResponse(data)
#     # data : {id: 1,name: "Upin Ipin Movie",desc: "Kisah 2 Anak Botak",movie_status: true}
# '''