from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('subjects/<int:subject_id>/edit/', views.subject_edit, name='subject_edit'),  # Edit existing subject
    path('subjects_list/', views.subject_list, name='subject_list'),
    path("subject_create/",views.subject_create,name="subject_create"), # List of subjects
    path('subject/<int:pk>/delete/', views.subject_delete, name='subject_delete'),

    
]