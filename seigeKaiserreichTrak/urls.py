from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('', include('apps.userprofile.urls')),
    path('', include('apps.team.urls')),
    path('', include('apps.project.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
