from django.db import models
class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    years_of_experience = models.PositiveIntegerField()
    date_joined = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='teacher_pics/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
