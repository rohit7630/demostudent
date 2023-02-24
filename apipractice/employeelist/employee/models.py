from django.db import models

class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=50,blank=False,null=False)
    emp_designation = models.CharField(max_length=50)
    emp_salary = models.IntegerField()
    emp_country = models.CharField(max_length=20)
    emp_state = models.CharField(max_length=30)
    emp_city = models.CharField(max_length=30)
    


