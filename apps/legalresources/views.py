# legalresources/views.py

from rest_framework import viewsets
from .models import LegalResource
from .serializers import LegalResourceSerializer
from .permissions import IsAdminOrReadOnly

class LegalResourceViewSet(viewsets.ModelViewSet):
    queryset = LegalResource.objects.all().order_by('-created_at')
    serializer_class = LegalResourceSerializer
    permission_classes = [IsAdminOrReadOnly]
