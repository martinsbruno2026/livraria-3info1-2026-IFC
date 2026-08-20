# pylint: disable=import-error
# pyright: reportMissingImports=false
from rest_framework import serializers  # type: ignore[import-not-found]

from core.models import Livro
from uploader.models import Image
from uploader.serializers import ImageSerializer


class LivroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = (
            'id',
            'titulo',
            'preco',
        )


class LivroRetrieveSerializer(serializers.ModelSerializer):
    capa = ImageSerializer(
        required=False,
        read_only=True,
    )

    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1


class LivroSerializer(serializers.ModelSerializer):
    capa_attachment_key = serializers.SlugRelatedField(
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )

    capa = ImageSerializer(
        required=False,
        read_only=True,
    )

    class Meta:
        model = Livro
        fields = '__all__'
