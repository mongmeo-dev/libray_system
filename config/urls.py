from django.conf.urls import static
from django.contrib import admin
from django.urls import path

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
