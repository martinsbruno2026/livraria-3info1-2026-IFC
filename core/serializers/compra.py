from rest_framework.serializers import ModelSerializer, CharField
from core.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = CharField(read_only=True)

    class Meta:
        model = ItensCompra
        fields = ("id", "compra", "livro", "quantidade", "total")

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
