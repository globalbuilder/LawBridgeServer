# users/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer
from .permissions import IsOwnerOrReadOnlyProfile

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for a user to view or update their own profile.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Restrict queryset to only the current user's profile.
        return Profile.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        # There's only one profile per user. We fetch it.
        profile = self.get_queryset().first()
        if not profile:
            return Response({"detail": "No profile found."}, status=404)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    def perform_update(self, serializer):
        # Enforce that the profile belongs to the current user.
        serializer.save(user=self.request.user)

class RegisterView(APIView):
    """
    API endpoint for user registration.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "User registered successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
