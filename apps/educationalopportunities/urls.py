from django.urls import path
from .views import (
    EducationalOpportunityListView,
    EducationalOpportunityDetailView,
    FavoriteOpportunityListView,
    AddFavoriteOpportunityView,
    RemoveFavoriteOpportunityView
)

urlpatterns = [
    path('', EducationalOpportunityListView.as_view(), name='opportunity-list'),
    path('<int:pk>/', EducationalOpportunityDetailView.as_view(), name='opportunity-detail'),

    path('favorites/', FavoriteOpportunityListView.as_view(), name='favorite-list'),
    path('favorites/add/', AddFavoriteOpportunityView.as_view(), name='add-favorite'),
    path('favorites/remove/<int:opportunity_id>/', RemoveFavoriteOpportunityView.as_view(), name='remove-favorite'),
]
