from django.shortcuts import render
from django.urls import path
from django.contrib import admin
from .models import *

class CustomAdminSite(admin.AdminSite):
    site_header = "Custom Admin Dashboard"
    site_title = "Admin"
    index_title = "Welcome to the Admin Panel"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_dashboard, name='admin_dashboard'),
        ]
        return custom_urls + urls

    def admin_dashboard(self, request):
        teachers_count = Teacher.objects.count()
        return render(request, "admin/dashboard.html", {"teachers_count": teachers_count})

custom_admin_site = CustomAdminSite(name="custom_admin")

custom_admin_site.register(Teacher)
admin.site.register(Teacher)
