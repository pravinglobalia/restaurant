from ninja import Schema, ModelSchema
from api.models import *



class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['first_name', 'last_name', 'email', 'password', 'username']

class RestaurantSchema(ModelSchema):
    class Config:
        model = Restaurant
        model_fields = ['name','address','phone']
        read_only = ['id']