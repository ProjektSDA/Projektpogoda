from django.shortcuts import render, redirect
from .forms import MySignupForm


def register_view(request):
    if request.method == "POST":
        form = MySignupForm(request.POST)
        if form.is_valid():
            obj = form.cleaned_data
            form.save()
            return redirect("weather_base")
    form = MySignupForm()
    return render(request, "registration/register.html", {"form": form})
