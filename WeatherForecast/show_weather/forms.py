from django import forms
from django.core.exceptions import ValidationError


def is_alpha(self):
    if not self.isalpha():
        raise ValidationError("Location doesn't exist")


class LocationForm(forms.Form):
    location = forms.CharField(
        max_length=30,
        validators=[
            is_alpha,
        ],
    )
