from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Teacher
from .forms import TeacherForm
from django.http import HttpResponseForbidden
from student.models import Student
from subjects.models import Course,Assignment

def teacher_dashboard(request):
    # Fetch the data for the teacher
    total_courses = Course.objects.count()
    total_assignments = Assignment.objects.count()
    total_tests = 40  # This can be dynamic based on your app
    students_managed = Student.objects.count()
    
    # Fetch upcoming classes (courses with upcoming flag set to True)
    # upcoming_classes = Course.objects.filter(upcoming=True)
    
    context = {
        'total_courses': total_courses,
        'total_assignments': total_assignments,
        'total_tests': total_tests,
        'students_managed': students_managed,
        # 'upcoming_classes': upcoming_classes,
    }

    return render(request, 'Home/teachers/teacher_deshboard.html', context)

# List all teachers
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'Home/teachers/teacher_list.html', {'teachers': teachers})

# Retrieve a single teacher
def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'Home/teachers/teacher_details.html', {'teacher': teacher})

# Create a new teacher
def add_teacher(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        subject = request.POST.get('subject')
        years_of_experience = request.POST.get('years_of_experience')
        profile_picture = request.FILES.get('profile_picture')  # Handling file upload
        
        # Create and save the teacher to the database
        teacher = Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            gender=gender,
            date_of_birth=date_of_birth,
            subject=subject,
            years_of_experience=years_of_experience,
            profile_picture=profile_picture
        )
        # Redirect to teacher list or another page
        return redirect('teacher_list')  # Change 'teacher_list' to the appropriate URL name
        
    return render(request, 'Home/teachers/teacher_create.html')


# View to handle editing a teacher
def teacher_edit(request, teacher_id):
    # Fetch the teacher object by ID
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    
    if request.method == 'POST':
        # Handle form submission
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        subject = request.POST.get('subject')
        years_of_experience = request.POST.get('years_of_experience')
        profile_picture = request.FILES.get('profile_picture')  # Handling file upload if it's changed

        # Update the teacher data
        teacher.first_name = first_name
        teacher.last_name = last_name
        teacher.email = email
        teacher.phone_number = phone_number
        teacher.gender = gender
        teacher.date_of_birth = date_of_birth
        teacher.subject = subject
        teacher.years_of_experience = years_of_experience
        if profile_picture:
            teacher.profile_picture = profile_picture  # Update profile picture if provided
        teacher.save()  # Save the updated teacher data
        
        # Redirect to the teacher list or any other page
        return redirect('teacher_list')  # Change this URL name as necessary
    
    return render(request, 'Home/teachers/teacher_edit.html', {'teacher': teacher})

# Delete a teacher
def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == "POST":
        teacher.delete()
        return redirect('teacher_list')
    return HttpResponseForbidden()
