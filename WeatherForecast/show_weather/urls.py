from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.SubmitLocationView.as_view(),name='submit_location'),
    path("todays_weather/<location>/",views.ShowWeatherView.as_view(),name="todays_weather"),
]
