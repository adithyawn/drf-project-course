from django.urls import path, include
# import function from views OLD
# from watchlist_app.views import movie_list,movie_details
# import function from views DRF

# function based view
# from watchlist_app.api.views import movie_list , movie_details

# class based view
from watchlist_app.api.views import WatchListAV , WatchDetailAV, StreamPlatformListAV,StreamPlatformDetailAV,ReviewList,ReviewDetail

# function based view
# urlpatterns = [
#     # so it will be /movie/list
#     path('list/', movie_list, name='movie-list'),
#     path('<int:id>', movie_details, name='movie-details'),
# ]

# class based view
urlpatterns = [
    # so it will be /watch/list
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:id>', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream-list'),
    path('stream/<int:id>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('review/', ReviewList.as_view(), name='review-list'),
    # try using <int:pk>. Why not using <int:id> ? because it need setup lookup_field attribute in view, if use pk it doesnt need, django will recognize it. Better use pk instead
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]
