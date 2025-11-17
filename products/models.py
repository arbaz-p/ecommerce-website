from django.db import models
from django.conf import settings
# Create your models here.

class Product(models.Model):
    Seller=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    category=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name