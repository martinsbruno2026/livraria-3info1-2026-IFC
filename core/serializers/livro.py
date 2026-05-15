from rest_framework import serializers

from core.models import Livro
from uploader.models import Image
from uploader.serializers import ImageSerializer


class LivroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ('id', 'titulo', 'preco')


class LivroRetrieveSerializer(serializers.ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Livro
        fields = ('id', 'titulo', 'isbn', 'quantidade', 'preco', 'categoria', 'editora', 'autores', 'capa')
        depth = 1

class LivroSerializer(serializers.ModelSerializer):
    capa_attachment_key = serializers.SlugRelatedField(
        source='capa',
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Livro
        fields = (
            'id', 'titulo', 'isbn', 'quantidade', 'preco',
            'categoria', 'editora', 'autores', 'capa', 'capa_attachment_key'
        )

    capa = ImageSerializer(required=False, read_only=True)
