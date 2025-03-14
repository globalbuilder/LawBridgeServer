# favorites/views.py

from rest_framework import viewsets, permissions
from .models import FavoriteResource, FavoriteOpportunity
from .serializers import FavoriteResourceSerializer, FavoriteOpportunitySerializer

class FavoriteResourceViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show favorites for the currently authenticated user.
        return FavoriteResource.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteOpportunityViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteOpportunitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show favorites for the currently authenticated user.
        return FavoriteOpportunity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
