# admin.py
from django.contrib import admin
from .models import Manager

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'last_used', 'unique_id')  # Customize the fields displayed in the admin list view
