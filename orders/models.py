from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.

class Order(models.Model):
    STATUS_CHOICES=(
        ('pending','Pending'),
        ('paid','Paid'),
        ('shipped','Shipped'),
        ('delivered','Delivered')
    )

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}"
    


class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    Seller=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='sold_items',on_delete=models.SET_NULL,null=True)
    quantity=models.PositiveIntegerField()
    price_at_purchased=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
         return f"{self.product} × {self.quantity}"