from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['emp_id','emp_name','emp_designation','emp_salary','emp_country','emp_state','emp_city']
