from platform import platform
from django.db import models


# DATABASE RELATIONSHIP : https://docs.djangoproject.com/en/4.0/topics/db/examples/

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    # Return name when using StringRelatedField __str__ in serializers 

    def __str__(self):
        return self.name

# Create your models here.
class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    # One Movie only have One Platform. If the platform deleted then all movies related the platform will be deleted.
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    # Return title when using StringRelatedField __str__ in serializers 

    def __str__(self):
        return self.title