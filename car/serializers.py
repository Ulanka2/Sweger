from car.models import Car, CarDocument
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

     class Meta:
        model = User
        fields = ['id', 'username',]
       


class CarSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)
    worker = UserSerializer(read_only=True)
    
    class Meta:
        model = Car
        fields = ['owner', 'year_issue', 'maker', 'coutry', 'worker',]


class CarDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarDocument
        fields = ['car', 'file', 'status', ]

