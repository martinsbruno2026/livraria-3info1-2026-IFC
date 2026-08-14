from core.models import Compra
from rest_framework.serializers import ModelSerializer


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
