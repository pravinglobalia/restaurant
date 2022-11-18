from django.dispatch import receiver, Signal
from .models import *
from django.db.models.signals import post_save


like = Signal('request')

@receiver(like)
def total_like(sender, request, **kwargs):
    # print("*************USER**********",request.user)
    sender=sender
    # print(f"----------kwargs{kwargs}")
    # print("**********************",sender.id)
    print("---------------------------")
    print("-----------if--------------")
    restaurant=Restaurant.objects.get(id=sender.id)
    print("🚀🚀🚀🚀🚀🚀🚀🚀 ~ file: signals.py ~ line 14 ~ restaurant", restaurant.total_like)
    restaurant.total_like = restaurant.total_like + 1
    restaurant.like_by.add(request.user)
    restaurant.save()
    # else:
    #     print("----------else-------------")
    #     restaurant=Restaurant.objects.get(id=sender.id)
    #     print("🚀🚀🚀🚀🚀🚀🚀🚀 ~ file: signals.py ~ line 14 ~ restaurant", restaurant.total_like)
    #     restaurant.total_like = restaurant.total_like - 1
    #     restaurant.like_by.remove(request.user)
    #     restaurant.save()

unlike = Signal('request')
@receiver(unlike)
def total_unlike(sender,request, **kwargs):
    sender=sender
    restaurant = Restaurant.objects.get(id=sender.id)
    restaurant.total_like = restaurant.total_like - 1
    restaurant.like_by.remove(request.user)
    restaurant.save()
    restaurantlike = RestaurantLike.objects.filter(user=request.user).filter(restaurant__id=sender.id).first()
    print("🚀 ~ file: signals.py ~ line 39 ~ restaurantlike", restaurantlike)
    restaurantlike.delete()





# 2251429656