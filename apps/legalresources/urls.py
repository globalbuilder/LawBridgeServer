from django.urls import path
from .views import (
    LegalResourceListView,
    LegalResourceDetailView,
    FavoriteResourceListView,
    AddFavoriteResourceView,
    RemoveFavoriteResourceView
)

urlpatterns = [
    path('', LegalResourceListView.as_view(), name='resource-list'),
    path('<int:pk>/', LegalResourceDetailView.as_view(), name='resource-detail'),

    path('favorites/', FavoriteResourceListView.as_view(), name='favorite-list'),
    path('favorites/add/', AddFavoriteResourceView.as_view(), name='add-favorite'),
    path('favorites/remove/<int:resource_id>/', RemoveFavoriteResourceView.as_view(), name='remove-favorite'),
]
