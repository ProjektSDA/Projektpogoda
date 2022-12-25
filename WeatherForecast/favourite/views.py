from dataclasses import asdict

from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View

from favourite.models import Favourite
from favourite.entities import FavouriteEntity


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

        return redirect("favourite_list")


class FavouriteListView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        favourites = [x for x in Favourite.objects.filter(user=request.user)]
        return render(
            request,
            "favourite/favourite_list.html",
            context={"favourite_list": favourites},
        )
