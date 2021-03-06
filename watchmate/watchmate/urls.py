"""watchmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from logging.handlers import WatchedFileHandler
from django.contrib import admin
# import include to connect urls in watchmate with views.py in watchlist_app
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # state the path for watchlist_app OLD
    # path('movie/',include("watchlist_app.urls")),
    # state the path for watchlist_app/api USING DRF
    path('watch/',include("watchlist_app.api.urls")),
]
