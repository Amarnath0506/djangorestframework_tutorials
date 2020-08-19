from django.db import models

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=30)
    product_price = models.FloatField()
    product_color = models.CharField(max_length=20)
