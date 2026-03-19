from rest_framework import serializers

class AutorSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100, allow_blank=True, required=False)