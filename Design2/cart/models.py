from django.db import models

from shop.models import Product
from django.contrib.auth.models import User
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.product.price*self.quantity

    def __str__(self):
        return self.product.name
class Order_details(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_items=models.IntegerField()
    address=models.TextField(max_length=100)
    phone=models.BigIntegerField()
    pin=models.IntegerField()

    order_id=models.CharField(max_length=20)
    payment_status=models.CharField(max_length=20)
    delivery_status=models.CharField(max_length=20)
    ordered_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_id
class Payment(models.Model):
    name=models.CharField(max_length=20)
    amount=models.IntegerField()
    order_id=models.CharField(max_length=20)
    razorpay_payment_id=models.CharField(max_length=30,blank=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.order_id


