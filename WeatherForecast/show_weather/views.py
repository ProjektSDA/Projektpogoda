from dataclasses import asdict
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import View
from show_weather import forms
from show_weather.entities import FavouriteEntity
from show_weather.models import Weather, Favourite


class SubmitLocationView(View):
    def get(self, request):
        form = forms.LocationForm()
        return render(
            request,
            "show_weather/location_form.html",
            {"form": form, "title": "Choose location"},
        )

    def post(self, request):
        form = forms.LocationForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            location = (form["location"]).lower().capitalize()
            return redirect("todays_weather", location)
        return render(
            request,
            "show_weather/location_form.html",
            {"form": form, "title": "Choose location"},
        )


class ShowWeatherView(View):
    def get(self, request, location):
        response = requests.get(f"https://wttr.in/{location}?format=j1")
        json_response = response.json()
        shortened_response = json_response["current_condition"][0]

        weather = Weather(
            location=location,
            temperature=float(shortened_response["temp_C"]),
            humidity=shortened_response["humidity"],
            precipitation=float(shortened_response["precipMM"]),
            pressure=shortened_response["pressure"],
            description=shortened_response["weatherDesc"][0]["value"],
            wind_direction=shortened_response["winddir16Point"],
            wind_speed=shortened_response["windspeedKmph"],
        )
        return render(
            request,
            "show_weather/todays_weather.html",
            {
                "Weather": weather,
            },
        )


class FavouriteCreateView(LoginRequiredMixin, View):

    login_url = "login"

    def get(self, request, location):
        response = requests.get(f"https://wttr.in/{location}?format=j1")
        json_response = response.json()
        nearest_area = json_response["nearest_area"][0]
        favourite_entity = FavouriteEntity(
            location=location,
            latitude=nearest_area["latitude"],
            longitude=nearest_area["longitude"],
            user=self.request.user,
        )
        try:
            Favourite.objects.create(**asdict(favourite_entity))
        except IntegrityError:
            pass

        return redirect("todays_weather", location)


class FavouriteListView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        favourites = [x for x in Favourite.objects.filter(user=request.user)]
        return render(
            request,
            "show_weather/favourite_list.html",
            context={"favourite_list": favourites},
        )
