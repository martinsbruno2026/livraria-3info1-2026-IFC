from django.db import transaction
from rest_framework.serializers import (
    CharField,
<<<<<<< HEAD
    CurrentUserDefault,
    DecimalField,
    HiddenField,
=======
    DecimalField,
>>>>>>> d1b4469a2e28cec8a54137d0ee4617a7b3b59603
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from core.models import Compra, ItensCompra

# ====================================================================
# Itens Compra
# ====================================================================


class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')

<<<<<<< HEAD
    def validate_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValidationError('A quantidade deve ser maior do que zero.')
        return quantidade

    def validate(self, item):
        if item['quantidade'] > item['livro'].quantidade:
            raise ValidationError('Quantidade de itens maior do que a quantidade em estoque.')
        return item

=======
>>>>>>> d1b4469a2e28cec8a54137d0ee4617a7b3b59603

class ItensCompraListSerializer(ModelSerializer):
    livro = CharField(source='livro.titulo', read_only=True)

    class Meta:
        model = ItensCompra
        fields = ('quantidade', 'livro')


class ItensCompraSerializer(ModelSerializer):
    titulo = CharField(source='livro.titulo', read_only=True)
    editora = CharField(source='livro.editora.nome', read_only=True)
    preco = DecimalField(
        source='livro.preco',
        max_digits=7,
        decimal_places=2,
        read_only=True,
    )
    capa = CharField(source='livro.capa.url', read_only=True)

    total = SerializerMethodField()

    def get_total(self, item):
        return item.livro.preco * item.quantidade

    class Meta:
        model = ItensCompra
        fields = ('id', 'titulo', 'editora', 'quantidade', 'preco', 'total', 'capa')


# ====================================================================
# Compra
# ====================================================================

class CompraCreateUpdateSerializer(ModelSerializer):
<<<<<<< HEAD
    usuario = HiddenField(default=CurrentUserDefault())
=======
>>>>>>> d1b4469a2e28cec8a54137d0ee4617a7b3b59603
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'itens')

    @transaction.atomic
    def create(self, validated_data):
        itens = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)
        return compra

    @transaction.atomic
    def update(self, compra, validated_data):
        itens = validated_data.pop('itens', None)
        if itens is not None:
            compra.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=compra, **item)
        return super().update(compra, validated_data)


class CompraListSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    itens = ItensCompraListSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'itens')


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    status = CharField(source='get_status_display', read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'itens')

]
...
    @transaction.atomic
    def create(self, validated_data):
        itens = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item['preco'] = item['livro'].preco # preço do livro no momento da compra
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra
...