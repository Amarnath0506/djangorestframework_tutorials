from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=120)
    disgnation = models.CharField(max_length=120)

    def __str__(self):
        return self.name
