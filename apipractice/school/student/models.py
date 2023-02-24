from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=40,blank=False,null= False)
    roll = models.IntegerField()
    city =models.CharField(max_length=40,blank=False,null= False)

