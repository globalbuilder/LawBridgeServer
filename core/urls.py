from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from documentation import APIDocumentationView


urlpatterns = [
    path('', APIDocumentationView.as_view(), name='api-documentation'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/educationalopportunities/', include('educationalopportunities.urls')),
    path('api/legalresources/', include('legalresources.urls')),
    path('api/notifications/', include('notifications.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
