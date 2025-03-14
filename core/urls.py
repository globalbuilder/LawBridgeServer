# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users endpoints
    path('api/users/', include('users.urls')),

    # Legal Resources
    path('api/legalresources/', include('legalresources.urls')),

    # Educational Opportunities
    path('api/educationalopportunities/', include('educationalopportunities.urls')),

    # Favorites
    path('api/favorites/', include('favorites.urls')),

    # Notifications
    path('api/notifications/', include('notifications.urls')),
]

# If you're using DEBUG mode and want to serve media in dev:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
