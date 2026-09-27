from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

# Page views
def home(request):
    return render(request, 'home.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')

def profile_page(request):
    return render(request, 'profile.html')

def logout_page(request):
    return render(request, 'logout.html')

def children_page(request):
    return render(request, 'children.html')

def ngos_page(request):
    return render(request, 'ngos.html')

def ngo_detail_page(request, ngo_id):
    return render(request, 'ngo_detail.html', {'ngo_id': ngo_id})

urlpatterns = [
    # Frontend pages
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('profile/', profile_page, name='profile'),
    path('children/', children_page, name='children'),
    path('ngos/', ngos_page, name='ngos'),
    path('ngo/<int:ngo_id>/', ngo_detail_page, name='ngo_detail'),

    # Admin
    path('admin/', admin.site.urls),

    # APIs
    path('api/auth/', include('apps.users.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)