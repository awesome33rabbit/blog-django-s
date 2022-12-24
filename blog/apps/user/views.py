from django.contrib import auth
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.serializers import UserSerializer
from django.contrib.auth.middleware import AuthenticationMiddleware
from rest_framework.permissions import AllowAny


# Create your views here.
class UserViews(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [AllowAny]

    tags = ["User"]


data = {
    "phone": "1232131",
    "password": "sda"
}
data.get("phone")

data = {
    "email": "asd@asd.com",
    "password": "sadas"
}
