
# apps/users/serializers.py

from rest_framework import serializers
from .models import User, NGO

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'email', 'phone', 'role', 'profile_photo', 'is_verified', 'created_at']
        read_only_fields = ['user_id', 'is_verified', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone', 'role']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class NGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = '__all__'
        read_only_fields = ['ngo_id', 'is_verified', 'created_at', 'updated_at']