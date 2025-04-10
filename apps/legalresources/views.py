from rest_framework import generics, status, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .models import LegalResource, FavoriteResource
from .serializers import LegalResourceSerializer, FavoriteResourceSerializer

class LegalResourceListView(generics.ListAPIView):

    queryset = LegalResource.objects.all().order_by('-created_at')
    serializer_class = LegalResourceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # Allow searching by title
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class LegalResourceDetailView(generics.RetrieveAPIView):

    queryset = LegalResource.objects.all()
    serializer_class = LegalResourceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class FavoriteResourceListView(generics.ListAPIView):

    serializer_class = FavoriteResourceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteResource.objects.filter(user=self.request.user)

class AddFavoriteResourceView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        resource_id = request.data.get('resource_id')
        if not resource_id:
            return Response(
                {"error": "resource_id is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            resource = LegalResource.objects.get(id=resource_id)
        except LegalResource.DoesNotExist:
            return Response(
                {"error": "LegalResource not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Check if it's already favorited
        favorite_exists = FavoriteResource.objects.filter(
            user=request.user,
            resource=resource
        ).exists()

        if favorite_exists:
            return Response(
                {"message": "Already in favorites."},
                status=status.HTTP_200_OK
            )

        # Create the favorite
        FavoriteResource.objects.create(
            user=request.user,
            resource=resource
        )
        return Response({"message": "Favorite added successfully."},
                        status=status.HTTP_201_CREATED)

class RemoveFavoriteResourceView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, resource_id):
        try:
            favorite = FavoriteResource.objects.get(
                user=request.user,
                resource_id=resource_id
            )
        except FavoriteResource.DoesNotExist:
            return Response(
                {"error": "Favorite does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        favorite.delete()
        return Response({"message": "Favorite removed successfully."},
                        status=status.HTTP_200_OK)
