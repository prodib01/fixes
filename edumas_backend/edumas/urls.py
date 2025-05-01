from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # path('academics/', include('academics.urls')),
    # path('attendance/', include('attendance.urls')),
    # path('health/', include('health.urls')),
    # path('timetable/', include('timetable.urls')),
    # path('core/', include('core.urls')),

    # 🔥 Swagger/OpenAPI routes
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


# Add media URL mapping in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)