from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    # Try to return name

    def __str__(self):
        return self.name