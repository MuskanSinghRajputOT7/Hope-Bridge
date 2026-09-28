from django.contrib import admin
from .models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['visitor_name', 'ngo', 'child', 'visit_date', 'visit_time', 'purpose', 'status']
