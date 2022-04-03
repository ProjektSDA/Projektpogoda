from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import MySignupForm


def register_view(request):
    if request.method == "POST":
        form = MySignupForm(request.POST)
        if form.is_valid():
            gotowe = form.cleaned_data
            print(gotowe)
            form.save()
            return redirect(to=reverse("main"))
    form = MySignupForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def main_view(request):
    return render(request, "main.html")
