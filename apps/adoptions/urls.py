from django.urls import path
from . import views

urlpatterns = [
    path('visit/book/', views.book_visit, name='book_visit'),
]
