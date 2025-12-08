from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'head_of_department', 'num_of_teachers', 'established_date', 'is_active']
    search_fields = ['name', 'head_of_department__first_name', 'head_of_department__last_name']
    list_filter = ['is_active', 'established_date']

admin.site.register(Department, DepartmentAdmin)
