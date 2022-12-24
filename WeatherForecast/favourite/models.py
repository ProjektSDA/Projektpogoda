from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User


class Favourite(models.Model):
    location = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")

    def __str__(self):
        return f"{self.user} favourite location : {self.location}"

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["latitude", "longitude", "user"], name="unique coordinates"
            )
        ]


# Create your models here.
