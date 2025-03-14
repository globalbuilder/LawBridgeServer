from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducationalOpportunityViewSet

router = DefaultRouter()
router.register(r'', EducationalOpportunityViewSet, basename='educationalopportunity')

urlpatterns = [
    path('', include(router.urls)),
]
