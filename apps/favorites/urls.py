# favorites/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteResourceViewSet, FavoriteOpportunityViewSet

router = DefaultRouter()
router.register(r'resources', FavoriteResourceViewSet, basename='favorite-resource')
router.register(r'opportunities', FavoriteOpportunityViewSet, basename='favorite-opportunity')

urlpatterns = [
    path('', include(router.urls)),
]
