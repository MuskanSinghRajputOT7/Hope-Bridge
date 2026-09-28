# apps/users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),              # ← NEW
    path('user/<int:user_id>/', views.get_user, name='get_user'),
    path('user/<int:user_id>/update/', views.update_profile, name='update_profile'),
    path('ngo/create/', views.create_ngo, name='create_ngo'),
    path('ngo/list/', views.list_ngos, name='list_ngos'),
    path('ngo/<int:ngo_id>/', views.get_ngo, name='get_ngo'),
]