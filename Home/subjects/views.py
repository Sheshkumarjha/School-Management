from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Course



def subject_list(request):
    subjects = Course.objects.all()  # Fetch all subjects from the database
    return render(request, 'Home/subjects/subjects.html', {'subject_list': subjects})
# View to create a new subject
def subject_create(request):
    if request.method == 'POST':
        # Manually handle form data
        name = request.POST.get('name')
        code = request.POST.get('code')
        description = request.POST.get('description')

        # Create a new subject instance and save it to the database
        new_subject = Course.objects.create(
            name=name,
            code=code,
            description=description
        )
        
        # After saving, redirect to the subject list page
        return redirect('subject_list')
    
    # If GET request, display an empty form
    return render(request, 'Home/subjects/subject_create.html')

def subject_edit(request, subject_id):
    # Get the existing subject or return a 404 error if not found
    subject = get_object_or_404(Course, pk=subject_id)

    if request.method == 'POST':
        # Manually handle form data
        name = request.POST.get('name')
        code = request.POST.get('code')
        description = request.POST.get('description')

        # Update the subject instance with the new data
        subject.name = name
        subject.code = code
        subject.description = description
        subject.save()  # Save the updated subject to the database
        
        # After saving, redirect to the subject list page
        return redirect('subject_list')

    # If GET request, prepopulate the form with the existing subject data
    return render(request, 'Home/subjects/subject_edit.html', {'subject': subject})

def subject_delete(request, pk):
    # Get the subject by primary key (pk)
    subject = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        # Delete the subject from the database
        subject.delete()
        # After deleting, redirect to the subject list page
        return redirect('subject_list')

    # If not POST, show a confirmation page
    return HttpResponseForbidden()