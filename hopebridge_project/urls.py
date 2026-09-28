from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static


# ============ PUBLIC PAGES ============
def login_page(request):
    # If already logged in, redirect to dashboard
    if request.session.get('user_id'):
        return redirect('/dashboard/')
    return render(request, 'login.html')


def register_page(request):
    if request.session.get('user_id'):
        return redirect('/dashboard/')
    return render(request, 'register.html')


# ============ PROTECTED PAGES ============
def home(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    return render(request, 'home.html')


def dashboard_page(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    return render(request, 'dashboard.html')


def profile_page(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    return render(request, 'profile.html')


def logout_page(request):
    # Clear session
    request.session.flush()
    return render(request, 'logout.html')


def children_page(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    return render(request, 'children.html')


def child_detail_page(request, child_id):
    if not request.session.get('user_id'):
        return redirect('/login/')
    return render(request, 'child_detail.html', {'child_id': child_id})


def ngos_page(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    return render(request, 'ngos.html')


def ngo_detail_page(request, ngo_id):
    if not request.session.get('user_id'):
        return redirect('/login/')
    return render(request, 'ngo_detail.html', {'ngo_id': ngo_id})


def adoption_guide_page(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    return render(request, 'adoption_guide.html')


def book_visit_page(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    return render(request, 'book_visit.html')


urlpatterns = [
    # Public pages
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),

    # Protected pages
    path('', home, name='home'),
    path('logout/', logout_page, name='logout'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('profile/', profile_page, name='profile'),
    path('children/', children_page, name='children'),
    path('child/<int:child_id>/', child_detail_page, name='child_detail'),
    path('ngos/', ngos_page, name='ngos'),
    path('ngo/<int:ngo_id>/', ngo_detail_page, name='ngo_detail'),
    path('adoption-guide/', adoption_guide_page, name='adoption_guide'),
    path('book-visit/', book_visit_page, name='book_visit'),

    # Admin
    path('admin/', admin.site.urls),

    # APIs
    path('api/auth/', include('apps.users.urls')),
    path('api/donations/', include('apps.donations.urls')),
    path('api/adoptions/', include('apps.adoptions.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)