from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import content.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('content.urls')),
    path('account/', include('account.urls')),
    path('rest-auth/', include('rest_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
