from django.db import models


class ProductList(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    price = models.FloatField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    image =models.CharField(max_length=150)
    rating = models.FloatField()

# Create your models here.
