# apps/users/admin.py

from django.contrib import admin
from .models import User, NGO

admin.site.register(User)
admin.site.register(NGO)
