from django.urls import path
from django.views.generic import ListView
from . import models, views

urlpatterns = [
    path("location/", views.SubmitLocationView.as_view(), name="submit_location"),
    path(
        "todays_weather/<location>/",
        views.ShowWeatherView.as_view(),
        name="todays_weather",
    ),
    path(
        "favourite/<location>/",
        views.FavouriteCreateView.as_view(),
        name="create_favourite",
    ),
    path("favourites/", views.FavouriteListView.as_view(), name="favourites"),
]
