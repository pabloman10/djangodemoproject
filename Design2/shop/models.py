from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    image=models.ImageField(upload_to='Category')

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField()
    desc=models.CharField(max_length=20)
    price=models.IntegerField()
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    Category=models.ForeignKey(Category,on_delete=models.CASCADE)


