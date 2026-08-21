try:
    from rest_framework import serializers  # type: ignore
except ImportError:

    class _DummySerializers:
        class ModelSerializer:
            pass

        class SlugRelatedField:
            def __init__(self, *args, **kwargs):  # noqa: ARG002
                pass

        class Serializer:
            pass

    serializers = _DummySerializers()

from core.models import Livro
from uploader.serializers import ImageSerializer

try:
    from uploader.models import Attachment
except ImportError:
    Attachment = None


class LivroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ('id', 'titulo', 'preco')


class LivroRetrieveSerializer(serializers.ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Livro
        fields = (
            'id',
            'titulo',
            'isbn',
            'quantidade',
            'preco',
            'categoria',
            'editora',
            'autores',
            'capa',
        )
        depth = 1


class LivroSerializer(serializers.ModelSerializer):
    if Attachment is not None:
        capa_attachment_key = serializers.SlugRelatedField(
            source='capa',
            slug_field='attachment_key',
            queryset=Attachment.objects.all(),
            required=False,
            write_only=True,
        )

    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Livro
        fields = (
            'id',
            'titulo',
            'isbn',
            'quantidade',
            'preco',
            'categoria',
            'editora',
            'autores',
            'capa',
        ) + (('capa_attachment_key',) if Attachment is not None else ())
