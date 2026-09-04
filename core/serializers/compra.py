from django.db import transaction
from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = CharField(read_only=True)

    class Meta:
        model = ItensCompra
        fields = ("id", "compra", "livro", "quantidade", "total")


class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")


class CompraCreateUpdateSerializer(ModelSerializer):
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "itens")
        read_only_fields = ("id",)

    @transaction.atomic
    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        return compra

    @transaction.atomic
    def update(self, instance, validated_data):
        itens_data = validated_data.pop("itens", None)
        instance = super().update(instance, validated_data)
        if itens_data is not None:
            instance.itens.all().delete()
            for item_data in itens_data:
                ItensCompra.objects.create(compra=instance, **item_data)
        return instance

from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,  # novo
    HiddenField,         # novo
    ModelSerializer,
    SerializerMethodField,
)