from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = '__all__'
       


        