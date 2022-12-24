from django.shortcuts import render, redirect
from django.views import View

from .forms import MySignupForm


class RegisterView(View):
    def post(self, request):
        form = MySignupForm(request.POST)
        if form.is_valid():
            obj = form.cleaned_data
            form.save()
            return redirect("submit_location")

    def get(self, request):
        form = MySignupForm()
        return render(request, "registration/register.html", {"form": form})
