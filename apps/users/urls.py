# users/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    # JWT endpoints
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Registration endpoint
    path('register/', RegisterView.as_view(), name='register'),
    # Profile endpoints
    path('', include(router.urls)),
]
