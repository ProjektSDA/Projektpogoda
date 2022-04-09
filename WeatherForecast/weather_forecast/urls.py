from django.contrib import admin

from django.urls import path, include

import show_weather

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user_service.urls")),
    path("show_weather/", include("show_weather.urls")),
    path("weatherforecast", show_weather.views.weather_base_view, name="weather_base"),
]
