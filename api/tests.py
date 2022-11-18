import pytest
from django.urls import reverse
from .models import User, Restaurant
from django.test import Client

# Create your tests here.

@pytest.fixture
def my_user(django_user_model):
    return django_user_model.objects.create_user(username="john", password="johnpassword", first_name="john", last_name="demo",email="john@gmail.com")

@pytest.fixture
def logged_in_client(client, my_user):
    return client.force_login(my_user)



#================ for register test ==============
@pytest.mark.django_db
def test_user_create(client):
    context = {
        'username': 'john',
        'password': 'johnpassword',
        'first_name': 'john',
        'last_name': 'demo',
        'email': 'gyan@gmail.com'
    }
    context1 = {
        'password2': "johnpassword",
        'username': 'john',
        'password': 'johnpassword',
        'first_name': 'john',
        'last_name': 'demo',
    }
    url = reverse('register')
    response = client.post(url, context)
    response1 = client.post(url, context1)
    assert response.status_code == 201
    assert response1.status_code == 400

# @pytest.mark.django_db
# def test_user_create():
#   user=User.objects.create_user(username='john', password='johnpassword')
#   assert User.objects.count() == 1
#   assert User.objects.get(username='john')
#   assert user.username == 'john'

#===================================== for login test ======================
@pytest.mark.django_db
def test_login_loginapi(client,my_user):
    context = {
        "username" : "john",
        "password":"johnpassword"
    }
    context1 = {
        "username": "john",
        "password":122
    }
    context2 ={
        "user":"john",
        "password":"johnpassword"
    }
    print("-----------------",context)
    url = reverse('login')
    print("*********************",url)
    response = client.post(url, context)
    response1= client.post(url, context1)
    assert response.status_code == 200
    assert response1.status_code == 400


#================= for restaurant test ======================
@pytest.mark.django_db
def test_restaurant(client,logged_in_client):
    context = {
        "name":"abc",
        "address":"suart",
        "phone":"1819865651"
    }
    context1 = Restaurant.objects.all()
    print("----------------",context)
    url = reverse('restaurant')
    print("🚀 ~ file: tests.py ~ line 76 ~ url", url)
    response = client.post(url, context)
    response1 = client.get(url,context1)
    assert response.status_code == 201
    assert response1.status_code == 200
