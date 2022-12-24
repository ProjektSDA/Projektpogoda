from django.urls import path

from favourite import views

urlpatterns = [
    path(
        "favourite/<location>/",
        views.FavouriteCreateView.as_view(),
        name="create_favourite",
    ),
    path("favourites/", views.FavouriteListView.as_view(), name="favourites"),
]
