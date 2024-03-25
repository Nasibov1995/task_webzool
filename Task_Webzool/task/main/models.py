from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    images = models.ImageField(upload_to="product")
    date = models.DateTimeField(default=timezone.now, db_index=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Comments(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Products, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name
