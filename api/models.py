from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    like = models.IntegerField(null=True)


class Restaurant(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    total_like=models.IntegerField(null=True,default=0)
    like_by=models.ManyToManyField(User, blank=True)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    food_name = models.CharField(max_length=255)
    food_details = models.CharField(max_length=255)
    price =models.IntegerField()

class RestaurantLike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="user")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)



