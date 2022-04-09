from django import forms
from django.core.exceptions import ValidationError


def is_alpha(self):
    if not self.isalpha():
        raise ValidationError("Location is not alpha !!!")


class LocationForm(forms.Form):
    location = forms.CharField(
        max_length=30,
        validators=[
            is_alpha,
        ],
    )


#
# class WeatherForm(forms.Form):
#     location = forms.CharField(max_length=30)
#     description = forms.CharField(max_length=20)
#     temperature = forms.IntegerField()
#     precipitation = forms.IntegerField()
#     pressure = forms.IntegerField()
#     wind_direction = forms.CharField(max_length=10)
#     wind_speed = forms.IntegerField()
#     humidity = forms.IntegerField()