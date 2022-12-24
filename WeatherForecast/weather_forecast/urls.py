from django.contrib import admin

from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user_service.urls")),
    path("show_weather/", include("show_weather.urls")),
]
