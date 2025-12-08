from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'gender', 'date_of_birth', 'subject', 'years_of_experience', 'profile_picture']
