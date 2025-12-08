from django.shortcuts import render, redirect,get_object_or_404
from .models import Department
from django.contrib import messages

from django.http import HttpResponseForbidden

def add_department(request):
    if request.method == 'POST':
        department_name = request.POST.get('name')
        department_description = request.POST.get('description')
        # Create a new department
        department = Department.objects.create(
            name=department_name,
            description=department_description
        )
        return redirect('list_department')
    return render(request, 'Home/department/add-department.html')

def list_department(request):
    department = Department.objects.all()  # Fetch all departments
    return render(request, 'Home/department/departments.html', {'department_list': department})


def edit_department(request, department_id):
    # Retrieve the department to edit
    department = get_object_or_404(Department, id=department_id)
    
    if request.method == 'POST':
        department_name = request.POST.get('name')
        department_description = request.POST.get('description')
        
        # Update the department
        department.name = department_name
        department.description = department_description
        department.save()  # Save the updated department
        
        # Redirect to the department list page
        return redirect('list_department')

    # Render the form with the current department data for editing
    return render(request, 'Home/department/edit-department.html', {'department': department})

def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)

    if request.method == "POST":
        department.delete()
        messages.success(request, "Department deleted successfully!")
        return redirect("list_department")  # Redirect after deletion

    return HttpResponseForbidden()

