from django.db import models

# Model for Fees Collection
class FeesCollection(models.Model):
    student_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_collected = models.DateField()
    receipt_number = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"Fees collected from {self.student_name}"

# Model for Expenses
class Expenses(models.Model):
    expense_category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_incurred = models.DateField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"Expense for {self.expense_category}"

# Model for Salary
class Salary(models.Model):
    employee_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    payment_mode = models.CharField(max_length=50)  # E.g., cash, bank transfer
    
    def __str__(self):
        return f"Salary paid to {self.employee_name}"
