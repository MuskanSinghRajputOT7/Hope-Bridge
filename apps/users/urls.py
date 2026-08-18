from django.urls import path
from . import views

# All user-related API endpoints
urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    
    # User profile
    path('user/<int:user_id>/', views.get_user, name='get_user'),
    path('user/<int:user_id>/update/', views.update_profile, name='update_profile'),
    
    # NGO management
    path('ngo/create/', views.create_ngo, name='create_ngo'),
    path('ngo/list/', views.list_ngos, name='list_ngos'),
]