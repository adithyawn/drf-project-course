from django.urls import path, include
# import function from views
from watchlist_app.views import movie_list,movie_details

urlpatterns = [
    # so it will be /movie/list
    path('list/', movie_list, name='movie-list'),
    path('<int:id>', movie_details, name='movie-details'),
]
