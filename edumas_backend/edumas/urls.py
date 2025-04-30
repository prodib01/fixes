from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    # path('academics/', include('academics.urls')),
    # path('attendance/', include('attendance.urls')),
    # path('health/', include('health.urls')),
    # path('timetable/', include('timetable.urls')),
    # path('core/', include('core.urls')),
]

# Add media URL mapping in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)