from django.urls import path
from .views import teacher_list, teacher_detail, add_teacher, teacher_edit, teacher_delete,teacher_dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/<int:teacher_id>/', teacher_detail, name='teacher_detail'),
    path('teachers/add/', add_teacher, name='teacher_create'),
    path('teachers/<int:teacher_id>/edit/', teacher_edit, name='teacher_update'),
    path('teachers/<int:teacher_id>/delete/', teacher_delete, name='teacher_delete'),
    path("Teacher",teacher_dashboard,name="teacher_dashboard")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
