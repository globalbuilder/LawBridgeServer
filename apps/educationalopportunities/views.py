from rest_framework import viewsets
from .models import EducationalOpportunity
from .serializers import EducationalOpportunitySerializer
from .permissions import IsAdminOrReadOnly

class EducationalOpportunityViewSet(viewsets.ModelViewSet):
    queryset = EducationalOpportunity.objects.all().order_by('-created_at')
    serializer_class = EducationalOpportunitySerializer
    permission_classes = [IsAdminOrReadOnly]
