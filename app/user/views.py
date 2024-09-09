"""
Views for the User API
"""
from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_cllass = UserSerializer
    