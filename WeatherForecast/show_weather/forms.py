from django import forms
from django.core.exceptions import ValidationError

from show_weather.models import Favourite


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


class FavouriteModelForm(forms.ModelForm):
    class Meta:
        model = Favourite
        fields = "__all__"
