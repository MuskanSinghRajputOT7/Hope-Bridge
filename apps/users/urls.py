from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user/<int:user_id>/', views.get_user, name='get_user'),
    path('ngo/create/', views.create_ngo, name='create_ngo'),
    path('ngo/list/', views.list_ngos, name='list_ngos'),
]