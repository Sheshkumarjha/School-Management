from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    # Use the correct app label if Teacher is in another app
    head_of_department = models.ForeignKey(
        'teachers.Teacher',  # Use '<app_name>.<model_name>'
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='head_of_departments'
    )

    num_of_teachers = models.PositiveIntegerField(default=0)
    established_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
