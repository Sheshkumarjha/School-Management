from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("Holiday/",views.holiday_list,name="holiday_list"),
    path("Holiday-Add/",views.add_holiday,name="add_holiday"),
    path('Holiday-edit/<int:holiday_id>/', views.edit_holiday, name='edit_holiday'),
    path('Holiday-delete/<int:holiday_id>/',views.delate_holiday, name='delete_holiday'),
    path("Exam-list/",views.exam_list,name="exam_list"),
    path("Exam-Add/",views.add_exam,name="add_exam"),
    path("Evant-list/",views.event_list, name="event_list"),
    path("Event-add/", views.add_event, name="add_event"),
    path("Event-edit/<int:event_id>/",views.edit_event, name="edit_event"),
    path("Event-delete/<int:event_id>/",views.delete_event, name="delete_event"),
    path("Timetable-list",views.timetable_list,name="timetable_list"),
    path("Timetable-add",views.add_timetable,name="add_timetable"),
    path('timetable-edit/<int:timetable_id>/', views.edit_timetable, name='edit_timetable'),
    path('timetable-delate/<int:timetable_id>/', views.delate_timetable, name='delate_timetable'),
    path("library-list",views.library_list,name="library_list"),
    path('library-add/', views.add_library, name='add_library'),
    path('library-edit/<int:library_id>/', views.edit_library, name='edit_library'),
    path('library-delete/<int:library_id>/', views.delete_library, name='delete_library'),
    path("Sports-list",views.sports_list,name="sports_list"),
    path("Sports-Add",views.add_sports,name="add_sports"),
    path("Sports-edit/<int:sports_id>/",views.edit_sports,name="edit_sports"),
    path("Sports-delate/<int:sports_id>/",views.delate_sports,name="delate_sports"),
    path("Hostel-list",views.hostel_list,name="hostel_list"),
    path("Hostel-Add",views.add_hostel,name="add_hostel"),
    path("Hostel-edit/<int:hostel_id>/",views.edit_hostel,name="edit_hostel"),
    path("Hostel-delate/<int:hostel_id>/",views.delate_hostel,name="delate_hostel")




   
]
