from rest_framework import generics, status, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .models import EducationalOpportunity, FavoriteOpportunity
from .serializers import (
    EducationalOpportunitySerializer,
    FavoriteOpportunitySerializer
)

class EducationalOpportunityListView(generics.ListAPIView):

    queryset = EducationalOpportunity.objects.all().order_by('-created_at')
    serializer_class = EducationalOpportunitySerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class EducationalOpportunityDetailView(generics.RetrieveAPIView):

    queryset = EducationalOpportunity.objects.all()
    serializer_class = EducationalOpportunitySerializer
    permission_classes = [permissions.IsAuthenticated]

class FavoriteOpportunityListView(generics.ListAPIView):

    serializer_class = FavoriteOpportunitySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteOpportunity.objects.filter(user=self.request.user)

class AddFavoriteOpportunityView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        opportunity_id = request.data.get('opportunity_id')
        if not opportunity_id:
            return Response(
                {"error": "opportunity_id is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            opportunity = EducationalOpportunity.objects.get(id=opportunity_id)
        except EducationalOpportunity.DoesNotExist:
            return Response(
                {"error": "Educational Opportunity not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Check if already favorited
        favorite_exists = FavoriteOpportunity.objects.filter(
            user=request.user,
            opportunity=opportunity
        ).exists()

        if favorite_exists:
            return Response(
                {"message": "Already in favorites."},
                status=status.HTTP_200_OK
            )

        # Create the favorite
        FavoriteOpportunity.objects.create(
            user=request.user,
            opportunity=opportunity
        )
        return Response({"message": "Favorite added successfully."},
                        status=status.HTTP_201_CREATED)

class RemoveFavoriteOpportunityView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, opportunity_id):
        try:
            favorite = FavoriteOpportunity.objects.get(
                user=request.user,
                opportunity_id=opportunity_id
            )
        except FavoriteOpportunity.DoesNotExist:
            return Response(
                {"error": "Favorite does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        favorite.delete()
        return Response({"message": "Favorite removed successfully."},
                        status=status.HTTP_200_OK)
