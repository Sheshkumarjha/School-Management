from django.db import models

# Holiday Model
class Holiday(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# Exam List Model
class ExamList(models.Model):
    exam_name = models.CharField(max_length=100)
    exam_date = models.DateField()
    subject = models.CharField(max_length=100)
    duration = models.DurationField()  # Duration of the exam
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.exam_name} ({self.subject})"

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    event_date = models.DateField()
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

# Timetable Model
class Timetable(models.Model):
    day_of_week = models.CharField(max_length=10)  # Example: Monday, Tuesday, etc.
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.day_of_week} - {self.subject}"

# Library Model
class Library(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    availability = models.BooleanField(default=True)  # Whether the book is available or not

    def __str__(self):
        return self.book_title

# Sports Model
class Sports(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    equipment_needed = models.TextField(null=True, blank=True)
    scheduled_date = models.DateField()

    def __str__(self):
        return self.name

# Hostel Model
class Hostel(models.Model):
    room_number = models.CharField(max_length=10)
    student_name = models.CharField(max_length=200)
    check_in_date = models.DateField()
    check_out_date = models.DateField(null=True, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} - {self.student_name}"

# Transport Model
class Transport(models.Model):
    vehicle_number = models.CharField(max_length=20)
    route = models.CharField(max_length=200)
    pick_up_time = models.TimeField()
    drop_off_time = models.TimeField()
    driver_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.vehicle_number} - {self.route}"

