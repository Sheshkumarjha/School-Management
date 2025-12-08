from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.http import HttpResponseForbidden



def fees_collection_list(request):
    fees = FeesCollection.objects.all()  # Get all FeesCollection records
    return render(request, 'Home/Accounts/fees_collection_list.html', {'fees': fees})

def fees_collection(request):
    fees = FeesCollection.objects.all()  # Get all FeesCollection records
    return render(request, 'Home/Accounts/fees.html', {'fees': fees})

def add_fees(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        amount = request.POST.get('amount')
        date_collected = request.POST.get('date_collected')
        receipt_number = request.POST.get('receipt_number')

        # Save to database
        FeesCollection.objects.create(
            student_name=student_name,
            amount=amount,
            date_collected=date_collected,
            receipt_number=receipt_number
        )
        return redirect('fees_collection_list')  # Redirect to list view after saving
    
    return render(request, 'Home/Accounts/add_fees.html')

def edit_fees(request, fee_id):
    fee = get_object_or_404(FeesCollection, id=fee_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        amount = request.POST.get('amount')
        date_collected = request.POST.get('date_collected')
        receipt_number = request.POST.get('receipt_number')

        # Update the existing record
        fee.student_name = student_name
        fee.amount = amount
        fee.date_collected = date_collected
        fee.receipt_number = receipt_number
        fee.save()

        return redirect('fees_collection_list')  # Redirect after saving changes

    # If not a POST request, render the edit form with the existing fee details
    return render(request, 'Home/Accounts/edit_fees.html', {'fee': fee})
    

def delete_fees(request, fee_id):
    fee = get_object_or_404(FeesCollection, id=fee_id)
    
    if request.method == "POST":
        fee.delete()
        return redirect('fees_collection_list')  # Redirect to the list after deletion

    return HttpResponseForbidden()

    
    # Render the edit form with the current fee data
    return render(request, 'Home/Accounts/edit_fees.html', {'fee': fee})

def eapenses(request):
    expenses=Expenses.objects.all()
    return render(request,"Home/Accounts/expenses.html",{"expenses":expenses})

def add_expenses(request):
    if request.method == 'POST':
        expense_category = request.POST.get('expense_category')
        amount = request.POST.get('amount')
        date_incurred = request.POST.get('date_incurred')
        description = request.POST.get('description')

        # Save to database
        Expenses.objects.create(
            expense_category=expense_category,
            amount=amount,
            date_incurred=date_incurred,
            description=description
        )
        return redirect('eapenses')  # Redirect to list view after saving
    
    return render(request, 'Home/Accounts/add_expenses.html')
def edit_expenses(request, expense_id):
    expense = get_object_or_404(Expenses, id=expense_id)

    if request.method == 'POST':
        expense.expense_category = request.POST.get('expense_category')
        expense.amount = request.POST.get('amount')
        expense.date_incurred = request.POST.get('date_incurred')
        expense.description = request.POST.get('description')

        expense.save()
        return redirect("expenses")  # Ensure this matches your URL name

    return render(request, "Home/Accounts/edit_eapenses.html", {"expense": expense})
def delete_expenses(request, expense_id):
    expense = get_object_or_404(Expenses, id=expense_id)
    if request.method == "POST":
        expense.delete()
        return redirect("expenses")
    return HttpResponseForbidden()
def salary(request):
    salaries = Salary.objects.all()
    return render(request, "Home/Accounts/salary.html", {"salaries": salaries})



def add_salary(request):
    if request.method == 'POST':
        employee_name = request.POST.get('employee_name')
        amount = request.POST.get('amount')
        date_paid = request.POST.get('date_paid')
        payment_mode = request.POST.get('payment_mode')

        # Save to database
        Salary.objects.create(
            employee_name=employee_name,
            amount=amount,
            date_paid=date_paid,
            payment_mode=payment_mode
        )
        return redirect('salary_list')  # Redirect to list view after saving
    
    return render(request, 'Home/Accounts/add_salary.html')
def edit_salary(request, salary_id):
    salary = get_object_or_404(Salary, id=salary_id)

    if request.method == 'POST':
        salary.employee_name = request.POST.get('employee_name')
        salary.amount = request.POST.get('amount')
        salary.date_paid = request.POST.get('date_paid')
        salary.payment_mode = request.POST.get('payment_mode')

        salary.save()  # Save the changes to the database
        return redirect('salary_list')  # Redirect to the salary list view after editing

    # Prepopulate the form with the current salary details
    return render(request, 'Home/Accounts/edit_salary.html', {'salary': salary})

def delete_salary(request, salary_id):
    salary = get_object_or_404(Salary, id=salary_id)

    if request.method == "POST":
        salary.delete()  # Delete the salary record
        return redirect('salary_list')  # Redirect to the salary list view after deletion
    
    return HttpResponseForbidden()