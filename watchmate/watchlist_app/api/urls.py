from django.urls import path, include
# import function from views OLD
# from watchlist_app.views import movie_list,movie_details
# import function from views DRF

# function based view
# from watchlist_app.api.views import movie_list , movie_details

# class based view
from watchlist_app.api.views import WatchListAV , WatchDetailAV, StreamPlatformListAV

# function based view
# urlpatterns = [
#     # so it will be /movie/list
#     path('list/', movie_list, name='movie-list'),
#     path('<int:id>', movie_details, name='movie-details'),
# ]

# class based view
urlpatterns = [
    # so it will be /movie/list
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:id>', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream')
]
