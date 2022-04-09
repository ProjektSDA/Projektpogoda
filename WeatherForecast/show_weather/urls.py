from django.urls import path

from show_weather import views

urlpatterns = [
    path("todays_weather/<city>/", views.show_weather_view, name="todays_weather"),
    path("form/", views.submit_city_view, name="submit_city"),
]
