from rest_framework.serializers import ModelSerializer, CharField
from core.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name", "foto")
        read_only_fields = ("id",)

class UserRegistrationSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("id", "email", "name", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
