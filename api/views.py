from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from api.serializer import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.signals import *
import datetime
import jwt
from django.conf import settings
from rest_framework import status


# Create your views here.
class RegisterApiview(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'user register'}, status=status.HTTP_201_CREATED)


class LoginApiview(APIView):
    serializer_class = LoginSerializer
    show_user = ShowUserinfo

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            username = serializer.data.get('username')
            password = serializer.data.get('password') 
            user = authenticate(username=username, password=password)
            user_serializer = self.show_user(user)
            token = RefreshToken.for_user(user)
            data = {
                'refresh': str(token),
                "access": str(token.access_token),
                'user_serializer': user_serializer.data
            }
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "please check you data"},status=status.HTTP_400_BAD_REQUEST)

def Generate_access_token(user):

    access_token_payload = {
        'user_id': user,
        'exp': datetime.datetime.utcnow()+datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(
        access_token_payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')

    return access_token


def Generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user,
        'exp': datetime.datetime.utcnow()+datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256').decode('utf-8')

    return refresh_token
class RestaurantAPi(APIView):
    permission_classes = [IsAuthenticated]
    serializers_classes = RestaurantSerializer

    def get(self,request):
        # restaurant = Restaurant.objects.filter(like_by__id=request.user.id)
        restaurant = Restaurant.objects.all()
        serializer = self.serializers_classes(restaurant,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=self.serializers_classes(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Restaurant Created."},status=status.HTTP_201_CREATED)


class MenuApi(APIView):
    serializer_classes = MenuSerializer

    def get(self,request, id):
        # restaurant =Restaurant.objects.filter(id=id)
        # print("🚀 ~ file: views.py ~ line 63 ~ restaurant", restaurant)
        menu = Menu.objects.filter(restaurant__id=id)
        print("🚀 ~ file: views.py ~ line 65 ~ menu", menu)
        serializer =self.serializer_classes(menu,many=True)
        return Response(serializer.data)


    def post(self,request,id):
        restaurant = Restaurant.objects.filter(id=id).first()
        if restaurant:
            serializer = self.serializer_classes(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(restaurant=restaurant)
            return Response({"message":"menu created"})
        else:
            return Response({"message":" Restaurant Not found"})

class RestaurantLikeApi(APIView):
    permission_classes =[IsAuthenticated]
    serializer_classes = RestaurantLikeSerializer

    def get(self, request):
        restaurant_like=RestaurantLike.objects.filter(user=request.user)
        serializer=self.serializer_classes(restaurant_like,many=True)
        print("🚀 ~ file: views.py ~ line 87 ~ serializer", serializer.data)
        return Response(serializer.data)

    def post(self,request,id):
        user=request.user
        print("🚀 ~ file: views.py ~ line 83 ~ user", user)
        restaurantlike = RestaurantLike.objects.filter(user=request.user).filter(restaurant__id=id).first()
        print("🚀🚀🚀🚀🚀🚀🚀🚀 ~ file: views.py ~ line 120 ~ restaurantlike", restaurantlike)
        restaurant = Restaurant.objects.filter(id=id).first()
        if restaurantlike is None:
            if restaurant:
                data = {
                    "data":restaurant.id
                }
                serializer = self.serializer_classes(data=data)
                like.send(sender=restaurant,request=request)
                serializer.is_valid(raise_exception=True)
                serializer.save(user=user, restaurant=restaurant)

                print('-----------request++++++++++request--------------------',request)
                return Response({"message":"liked."})
            else:
                return Response({"message":"Restaurant Not Found."})
        else:
            unlike.send(sender=restaurant,request=request)
            return Response({"message":"Unliked."})



# class TotalLikeApi(APIView):
#     serializer_classes= RestaurantSerializer

#     def get(self,request):
#         # seriali
#         pass