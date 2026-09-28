
from django.urls import path
from . import views

urlpatterns = [
    path('children/', views.list_children, name='list_children'),
    path('child/<int:child_id>/', views.get_child, name='get_child'),
]