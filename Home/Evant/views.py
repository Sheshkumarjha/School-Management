from django.shortcuts import render,get_object_or_404,redirect
from .models import Holiday, ExamList, Event, Timetable, Library, Sports, Hostel, Transport
from datetime import timedelta
# from django.http import JsonResponse
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# Holiday List View
def holiday_list(request):
    holidays = Holiday.objects.all()
    return render(request, "Home/ALL/holiday_list.html", {"holidays": holidays})
# return tha data in json formate
# @api_view(['GET'])  # Ensure this decorator is added
# def holiday_list(request):
#     holidays = Holiday.objects.all()  # Fetch all holidays
#     serializer = HolidaySerializer(holidays, many=True)  # Serialize data
#     return Response(serializer.data)

def add_holiday(request):
    if request.method == "POST":
        name=request.POST.get("name")
        start_date=request.POST.get("start_date")
        end_date=request.POST.get("end_date")
        description=request.POSt.get("description")
        Holiday.objects.create(
            name=name,
            start_date=start_date,
            end_date=end_date,
            description=description
        )
        return redirect("holiday_list")
    return render(request,"Home/ALL/add_holiday.html")

def edit_holiday(request, holiday_id):
    holiday = get_object_or_404(Holiday, id=holiday_id)  # Fetch holiday
    if request.method == "POST":
        holiday.name = request.POST.get("name")
        holiday.start_date = request.POST.get("start_date")
        holiday.end_date = request.POST.get("end_date")
        holiday.description = request.POST.get("description")
        holiday.save()
        return redirect("holiday_list")

    return render(request, "Home/ALL/edit_holiday.html", {"holiday": holiday})


def delate_holiday(request,holiday_id):
    holiday=get_object_or_404(Holiday,id=holiday_id)
    holiday.delete()
    return redirect("holiday_list")

# Exam List View
def exam_list(request):
    exams = ExamList.objects.all()
    return render(request, "Home/ALL/exam_list.html", {"exams": exams})

def add_exam(request):
    if request.method == "POST":
        exam_name = request.POST.get("exam_name")
        exam_date = request.POST.get("exam_date")
        subject = request.POST.get("subject")
        duration = request.POST.get("duration")  # Duration in HH:MM:SS format
        location = request.POST.get("location")

        # Convert duration to timedelta
        duration_parts = duration.split(":")
        if len(duration_parts) == 3:
            hours, minutes, seconds = map(int, duration_parts)
            duration_value = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        else:
            duration_value = timedelta(hours=0, minutes=0, seconds=0)  # Default to 0

        # Create Exam object
        ExamList.objects.create(
            exam_name=exam_name,
            exam_date=exam_date,  # Ensure format is YYYY-MM-DD
            subject=subject,
            duration=duration_value,
            location=location
        )

        return redirect("exam_list")

    return render(request, "Home/ALL/add_exam.html")
# Events List View

def event_list(request):
    event = Event.objects.all()
    return render(request, "Home/ALL/event_list.html", {"event": event})


def add_event(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        event_date = request.POST.get("event_date")
        location = request.POST.get("location")

        Event.objects.create(
            title=title,
            description=description,
            event_date=event_date,
            location=location
        )
        return redirect("event_list")

    return render(request, "Home/ALL/add_event.html")

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Ensure the right model is used

    if request.method == "POST":
        event.title = request.POST.get("title")
        event.description = request.POST.get("description")
        event.event_date = request.POST.get("event_date")
        event.location = request.POST.get("location")
        event.save()
        return redirect("event_list")  # Ensure event_list is correctly named in urls.py

    return render(request, "Home/ALL/edit_event.html", {"event": event})
# View for deleting an event
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect("event_list")

# Timetable View
def timetable_list(request):
    timetables = Timetable.objects.all()
    return render(request, "Home/ALL/timetable_list.html", {"timetables": timetables})

def add_timetable(request):
    if request.method == "POST":
        day_of_week=request.POST.get("day_of_week")
        start_time=request.POST.get("start_time")
        end_time=request.POST.get("end_time")
        subject=request.POST.get("subject")
        teacher=request.POST.get("teacher")
        Timetable.objects.create(
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time,
            subject=subject,
            teacher=teacher
        )
        return redirect("timetable_list")
    return render(request,"Home/ALL/add_timetable.html")

def edit_timetable(request,timetable_id):
    timetables=get_object_or_404(Timetable,id=timetable_id)
    if request.method == "POST":
        timetables.day_of_week=request.POST.get("day_of_week")
        timetables.start_time=request.POST.get("start_time")
        timetables.end_time=request.POST.get("end_time")
        timetables.subject=request.POST.get("subject")
        timetables.teacher=request.POST.get("teacher")
        timetables.save()
        return redirect("timetable_list")
    return render(request,"Home/ALL/edit_timetable.html",{"timetables":timetables})

def delate_timetable(request,timetable_id):
    timetables=get_object_or_404(Timetable,id=timetable_id)
    timetables.delete()
    return redirect("timetable_list")
    

# Library Books List View
def library_list(request):
    library_books = Library.objects.all()  # Fetch all books
    return render(request, 'Home/ALL/list_library.html', {'library_books': library_books})

def add_library(request):
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        isbn = request.POST.get('isbn')
        availability = request.POST.get('availability') == 'on'  # Checkbox is checked if it is 'on'

        Library.objects.create(
            book_title=book_title,
            author=author,
            publication_date=publication_date,
            isbn=isbn,
            availability=availability
        )
        return redirect('library_list')  # Redirect to the library list page after adding the book

    return render(request, 'Home/ALL/add_library.html')

def edit_library(request, library_id):
    library = get_object_or_404(Library, id=library_id)

    if request.method == 'POST':
        library.book_title = request.POST.get('book_title')
        library.author = request.POST.get('author')
        library.publication_date = request.POST.get('publication_date')
        library.isbn = request.POST.get('isbn')
        library.availability = request.POST.get('availability') == 'on'

        library.save()
        return redirect('library_list')  # Redirect to library list after saving the changes

    return render(request, 'Home/ALL/edit_library.html', {'library': library})

def delete_library(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    library.delete()  # Delete the library record
    return redirect('library_list')  # Redirect to library list after deletion



# Sports List View
def sports_list(request):
    sports = Sports.objects.all()
    return render(request, "Home/ALL/sports_list.html", {"sports": sports})

def add_sports(request):
    if request.method == "POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        equipment_needed=request.POST.get("equipment_needed")
        scheduled_date=request.POST.get("scheduled_date")
        Sports.objects.create(
            name=name,
            description=description,
            equipment_needed=equipment_needed,
            scheduled_date=scheduled_date

        )
        return redirect("sports_list")
    return render(request,"Home/All/add_sports.html")

def edit_sports(request,sports_id):
    sports=get_object_or_404(Sports,id=sports_id)
    if request.method == "POST":
        sports.name=request.POST.get("name")
        sports.description=request.POST.get("description")
        sports.equipment_needed=request.POST.get("equipment_needed")
        sports.scheduled_date=request.POST.get("scheduled_date")
        sports.save()
        return redirect("sports_list")
    return render(request,"Home/ALL/edit_sports.html",{"sports":sports})

def delate_sports(request,sports_id):
    sports=get_object_or_404(Sports,id=sports_id)
    sports.delete()
    return redirect("sports_list")



# Hostel List View
def hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, "Home/ALL/hostel_list.html", {"hostels": hostels})


def add_hostel(request):
    if request.method == "POST":
        room_number=request.POST.get("room_number")
        student_name =request.POST.get("student_name")
        check_in_date =request.POST.get("check_in_date")
        check_out_date=request.POST.get("check_out_date")
        fee=request.POST.get("fee")
        Hostel.objects.create(
            room_number=room_number,
            student_name=student_name,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            fee=fee
        )
        return redirect("hostel_list")
    return render(request,"Home/ALL/add_hostel.html")

def edit_hostel(request,hostel_id):
    hostels=get_object_or_404(Hostel,id=hostel_id)
    if request.method == "POST":
        hostels.room_number=request.POST.get("room_number")
        hostels.student_name =request.POST.get("student_name")
        hostels.check_in_date =request.POST.get("check_in_date")
        hostels.check_out_date=request.POST.get("check_out_date")
        hostels.fee=request.POST.get("fee")
        hostels.save()
        return redirect("hostel_list")
    return render(request,"Home/ALL/edit_hostel.html",{"hostels":hostels})

def delate_hostel(request,hostel_id):
    hostels=get_object_or_404(Hostel,id=hostel_id)
    hostels.delete()
    return redirect("hostel_list")



# Transport List View
def transport_list(request):
    transports = Transport.objects.all()
    return render(request, "Home/Transport/transport_list.html", {"transports": transports})

def add_trensport(request):
    pass
