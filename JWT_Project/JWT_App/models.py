from django.db import models

class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.empname

