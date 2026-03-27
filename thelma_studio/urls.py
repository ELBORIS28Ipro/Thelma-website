from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Pressed by Thelma — Admin"
admin.site.site_title = "Pressed by Thelma"
admin.site.index_title = "Manage Your Website"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
