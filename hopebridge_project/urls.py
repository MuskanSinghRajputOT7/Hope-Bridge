from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

# Homepage view
def home_page(request):
    return render(request, 'home.html')

# Main URL patterns
urlpatterns = [
    path('', home_page, name='home'),           # Homepage
    path('admin/', admin.site.urls),            # Admin panel
    path('api/auth/', include('apps.users.urls')),  # Include users app URLs
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)