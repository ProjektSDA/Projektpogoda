import requests
from django.shortcuts import render, redirect
from django.views.generic import View

from constans import WTTR_URL, RESPONSE_FORMAT
from show_weather import forms
from show_weather.models import Weather


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
        response = requests.get(f"{WTTR_URL}{location}?format={RESPONSE_FORMAT}")
        json_response = response.json()
        current_condition = json_response["current_condition"][0]

        weather = Weather(
            location=location,
            temperature=float(current_condition["temp_C"]),
            humidity=current_condition["humidity"],
            precipitation=float(current_condition["precipMM"]),
            pressure=current_condition["pressure"],
            description=current_condition["weatherDesc"][0]["value"],
            wind_direction=current_condition["winddir16Point"],
            wind_speed=current_condition["windspeedKmph"],
        )
        return render(
            request,
            "show_weather/todays_weather.html",
            {
                "Weather": weather,
            },
        )
