from django.contrib import admin
from django.urls import path,include
from .import views 

urlpatterns = [
    path('add-fees/', views.add_fees, name='add_fees'),
    path('fees/', views.fees_collection_list, name='fees_collection_list'),
    path('fees/edit/<int:fee_id>/',views.edit_fees, name='edit_fees'),
    path('fees/delete/<int:fee_id>/',views.delete_fees, name='delete_fees'),
    path('add-expenses/', views.add_expenses, name='add_expenses'), 
    path("Expenses/",views.eapenses,name="eapenses"),
    path("expenses/edit/<int:expense_id>/",views.edit_expenses,name="edit_expenses"),
    path("Expenses/delate/<int:expense_id>",views.delete_expenses ,name="delate_expenses"),
    path('add-salary/', views.add_salary, name='add_salary'),
    path("fees/Student",views.fees_collection,name="fees"),
    path('salary/edit/<int:salary_id>/',views.edit_salary, name='edit_salary'),
    path("Salary/List",views.salary,name="salary_list"),
    path('salary/Delate/<int:salary_id>/',views.delete_salary, name='delete_salary'),




]