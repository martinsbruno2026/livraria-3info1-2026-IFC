from rest_framework import serializers

from core.models import Editora


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'
