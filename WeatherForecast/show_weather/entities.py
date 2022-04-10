from dataclasses import dataclass

from django.contrib.auth import get_user_model

User = get_user_model()


@dataclass
class FavouriteEntity:
    location: str
    latitude: float
    longitude: float
    user: User
