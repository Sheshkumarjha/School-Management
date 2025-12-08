from django.http import HttpResponse,HttpResponseForbidden
from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification    
from teachers.models import Teacher
from jome_auth.models import CustomUser


# Create your views here.

def index(request):
    teachers_count = Teacher.objects.count()
    students_count = CustomUser.objects.filter(groups__name='Students').count()  # Modify as per your Student model
    unread_notifications = Notification.objects.filter(is_read=False)
    unread_notification_count = unread_notifications.count()

    context = {
        'teachers_count': teachers_count,
        'students_count': students_count,
        'unread_notification': unread_notifications,
        'unread_notification_count': unread_notification_count,
    }
    return render(request, "Home/index.html")
#create student dashboard view
def student_dashboard(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()
    return render(request, "Home/students/student-dashboard.html")


def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        notification = Notification.objects.filter(user=request.user)
        notification.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden