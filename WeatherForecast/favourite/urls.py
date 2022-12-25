from django.urls import path, reverse_lazy
from django.views.generic import DeleteView

from favourite import views
from favourite.models import Favourite

urlpatterns = [
    path(
        "favourite/<location>/",
        views.FavouriteCreateView.as_view(),
        name="create_favourite",
    ),
    path("favourites/", views.FavouriteListView.as_view(), name="favourite_list"),
    path('favourite_delete/<int:idx>/', DeleteView.as_view(model=Favourite, success_url=reverse_lazy('favourite_list'), pk_url_kwarg='idx'),
         name='favourite_delete')
]
