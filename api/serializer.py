from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LikeByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=254)
    password = serializers.CharField(max_length=254)
    class Meta:
        model = User
        fields = ['username', 'password']


class ShowUserinfo(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class RestaurantSerializer(serializers.ModelSerializer):
    # like_by = LikeByUserSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = ['id', 'name','address','phone','total_like', 'like_by']

    # def director(self):
    #     test = ",".join([str(p) for p in self.user.all()])
    #     user = User.objects.get(username=test)
    #     return user.first_name + " " + user.last_name


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields =['id', 'food_name', 'food_details', 'price']


class RestaurantLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only= True)
    restaurant = RestaurantSerializer(read_only = True)
    class Meta:
        model = RestaurantLike
        fields =['user', 'restaurant']

