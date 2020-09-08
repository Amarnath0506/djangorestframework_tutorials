from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=120, unique=True)
    mobile_no = models.IntegerField(unique=True)
    address = models.CharField(max_length=120)
    problem = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=120, unique=True)
    designation = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient= models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()









