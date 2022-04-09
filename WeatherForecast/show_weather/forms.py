from django import forms


class CityForm(forms.Form):
    city = forms.CharField(max_length=30)


# stworzę form z models we viewsach
# class WeatherForm(forms.Form):
#     city = forms.CharField(max_length=30)
#     description = forms.CharField(max_length=20)
#     temperature = forms.IntegerField
#     precipitation = forms.IntegerField
#     pressure = forms.IntegerField
#     wind_direction = forms.CharField(max_length=10)
#     wind_speed = forms.IntegerField
#     humidity = forms.IntegerField
