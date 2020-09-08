from django.db import models

# Create your models here.
class Emp(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10 , decimal_places=2)