from ninja import Router
from ninja.security import django_auth
from api.schemas import UserSchema, RestaurantSchema
from api.models import User,Restaurant
from typing import List

router_api = Router()

@router_api.post("/user", tags=["user"])
def create_user(request, payload: UserSchema):
    data = payload.dict()
    print("🚀 ~ file: api.py ~ line 12 ~ data", data)
    user = User.objects.create(**data)
    user.set_password(data["password"])
    user.save()
    return {"id": user.id, "first_name": user.first_name}

@router_api.get("/user", response = List[UserSchema], auth = django_auth,tags=["user"])
def get(request):
   user = User.objects.all()
   return user

@router_api.post('/restaurant', tags=["restaurant"])
def post(request, payload: RestaurantSchema):
    data = payload.dict()
    restaurant = Restaurant.objects.create(**data)
    restaurant.save()
    return({"message":"Restaurabt created."})


@router_api.get('/restaurant', response = List[RestaurantSchema],tags=['restaurant'])
def get(request):
    restaurant = Restaurant.objects.all()
    return restaurant


