from django.contrib import admin
from .models import FeesCollection, Expenses, Salary

# Register your models here.

# Register FeesCollection model
class FeesCollectionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'amount', 'date_collected', 'receipt_number')  # Fields to display in the list
    search_fields = ('student_name', 'receipt_number')  # Add search functionality
    list_filter = ('date_collected',)  # Allow filtering by date_collected

# Register Expenses model
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('expense_name', 'amount', 'date_incurred', 'category')  # Fields to display in the list
    search_fields = ('expense_name', 'category')  # Add search functionality
    list_filter = ('date_incurred', 'category')  # Allow filtering by category and date_incurred

# Register Salary model
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'amount', 'date_paid', 'payment_mode')  # Fields to display in the list
    search_fields = ('employee_name', 'payment_mode')  # Add search functionality
    list_filter = ('date_paid', 'payment_mode')  # Allow filtering by date_paid and payment_mode

# Registering the models with the admin site
admin.site.register(FeesCollection)
admin.site.register(Expenses)
admin.site.register(Salary)
