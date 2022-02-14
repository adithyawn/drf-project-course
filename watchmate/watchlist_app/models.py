from platform import platform
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here. Add Model Field Options & Types https://docs.djangoproject.com/en/4.0/ref/models/fields/
class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    # Return name when using StringRelatedField __str__ in serializers 
    # str method will return string instead of class object (__repr__) by default, https://www.educative.io/edpresso/what-is-the-str-method-in-python    
    def __str__(self):
        return self.name

# Create your models here. Add Model Field Options & Types https://docs.djangoproject.com/en/4.0/ref/models/fields/
class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    # One Movie only have One Platform. If the platform deleted then all movies related the platform will be deleted.
    # DATABASE RELATIONSHIP : https://docs.djangoproject.com/en/4.0/topics/db/examples/
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    # Return title when using StringRelatedField __str__ in serializers 

    def __str__(self):
        return self.title

# Create your models here. Add Model Field Options & Types https://docs.djangoproject.com/en/4.0/ref/models/fields/
class Review(models.Model):
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1),MinValueValidator(5)])
    # Cannot Null (empty)
    description = models.CharField(max_length=200, null=True)
    # One Movie only have One Platform. If the platform deleted then all movies related the platform will be deleted.
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    # Automatically set the field to now when the object is first created.
    created = models.DateTimeField(auto_now_add=True)
    # Automatically set the field to now every time the object is saved. Useful for “last-modified” timestamps
    update = models.DateTimeField(auto_now=True)

    # Return rating when using StringRelatedField __str__ in serializers 

    def __str__(self):
        # must return string because rating is Integer need convert to Str
        return str(self.rating) + " | " + self.watchlist.title