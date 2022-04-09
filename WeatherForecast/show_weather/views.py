import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from show_weather.forms import CityForm
from show_weather.models import Weather


@login_required
def weather_base_view(request):
    return render(request, "show_weather/weather_base.html")


def submit_city_view(request):

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
        url = reverse("todays_weather", kwargs={"city": city})
        return redirect(url)
    elif request.method == "GET":
        form = CityForm()
        return render(request, "show_weather/form.html", {"form": form})


def show_weather_view(request, city):
    if request.method == "GET":
        response = requests.get(f"https://wttr.in/{city}?format=j1")
        json_response = response.json()
        shortened_response = json_response["current_condition"][0]

        weather = Weather(
            city=city,
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


# Create your views here.
