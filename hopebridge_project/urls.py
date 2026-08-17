from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple homepage function (NO imports from views.py)
def home_page(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>HopeBridge</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; }
            a { color: blue; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>🚀 HopeBridge</h1>
        <p>Child Support & Adoption Assistance Platform</p>
        <ul style="list-style: none; padding: 0;">
            <li><a href='/admin/'>🔐 Admin Panel</a></li>
            <li><a href='/api/auth/login/'>🔑 Login API</a></li>
            <li><a href='/api/auth/register/'>📝 Register API</a></li>
        </ul>
        <p style="margin-top: 30px; color: green;">✅ Server is running!</p>
    </body>
    </html>
    """)

urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.users.urls')),
]