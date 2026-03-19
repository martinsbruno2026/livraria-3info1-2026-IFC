from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models
from rest_framework import serializers

from rest_framework import viewsets
from core.models import Autor   # ← importe o modelo daqui
from core.serializers import AutorSerializer  # ajuste o caminho se necessário

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    # filterset_fields = ['nome']
    # search_fields = ['nome']


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome', 'email']

