from django.db import models

# Create your models here.
class Paragism(models.Model):
    name = models.CharField(max_length=120, verbose_name="name")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=120)
    paragism = models.ForeignKey(Paragism, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=120)
    laguage = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
