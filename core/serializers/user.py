
try:
    from rest_framework import serializers
except ImportError as e:
    raise ImportError(
        "Missing dependency: djangorestframework is required to use core.serializers.user; "
        "install it with `pip install djangorestframework`."
    ) from e

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'groups']
        depth = 1


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['email', 'name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
