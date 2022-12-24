from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password_reset", PasswordResetView.as_view()),
    path(
        "password_reset_done",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("registration", views.RegisterView.as_view(), name="registration"),
]
