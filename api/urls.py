from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.RegisterApiview.as_view(),name='register'),
    path('login/',views.LoginApiview.as_view(),name='login'),
    path('restaurant/',views.RestaurantAPi.as_view(),name='restaurant'),
    path('menu/<int:id>/',views.MenuApi.as_view(),name='menu'),
    path('like/<int:id>/',views.RestaurantLikeApi.as_view(),name='like'),
    path('unlike/',views.RestaurantLikeApi.as_view(),name='unlike'),
]