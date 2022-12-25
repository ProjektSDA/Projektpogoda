from django import forms
from django.core.exceptions import ValidationError

from favourite.models import Favourite


def is_alpha(self):
    if not self.isalpha():
        raise ValidationError("Location is not alpha !!!")


class LocationForm(forms.Form):
    location = forms.CharField(
        max_length=30,
        
    )
