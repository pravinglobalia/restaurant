from django.contrib import admin
from api.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display =('id', 'username', 'first_name', 'last_name', 'email')


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone']

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'food_name', 'food_details', 'price', 'restaurant_name', 'address']

    def restaurant_name(self, obj):
        return obj.restaurant.name
    def address(self, obj):
        return obj.restaurant.address

class RestaurantLikeAdmin(admin.ModelAdmin):
    list_display= ['user', 'restaurant_name']

    def restaurant_name(self, obj):
        return obj.restaurant.name


admin.site.register(User, UserAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(RestaurantLike, RestaurantLikeAdmin)


