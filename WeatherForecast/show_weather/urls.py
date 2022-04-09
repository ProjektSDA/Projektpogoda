from django.urls import path, reverse_lazy
from django.views.generic import CreateView
from . import models, forms

from . import views

urlpatterns = [
    path('form/',views.SubmitLocationView.as_view(),name='submit_location'),
    path("todays_weather/<location>/",views.ShowWeatherView.as_view(),name="todays_weather"),
    path('favorite/',CreateView.as_view(form_class=forms.Favorite,template_name='show_weather/favorite_form.html',success_url=reverse_lazy('favorite'))),
]
