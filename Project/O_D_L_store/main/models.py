from django.db import models

# models.py

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    shape = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/main/products/')

    def __str__(self):
        return self.name
