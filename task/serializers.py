from rest_framework import serializers
from .models import Registration
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

