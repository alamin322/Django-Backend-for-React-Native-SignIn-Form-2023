from rest_framework import serializers
from .models import SignIn

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignIn
        fields = ('user_email', 'password')