from rest_framework import serializers

from core.models import Livro
from uploader.models import Image
from uploader.serializers import ImageSerializer


class LivroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
<<<<<<< HEAD
        fields = ('id', 'titulo', 'preco')


class LivroRetrieveSerializer(serializers.ModelSerializer):
=======
        fields = '__all__'  # ou liste os campos: ['id', 'titulo', 'isbn', 'quantidade', 'preco']

        ...
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer
...
class LivroRetrieveSerializer(ModelSerializer):
>>>>>>> 289b2b8760bcde2e74635f8492ad2e3ddcee4bfd
    capa = ImageSerializer(required=False)

    class Meta:
        model = Livro
<<<<<<< HEAD
        fields = ('id', 'titulo', 'isbn', 'quantidade', 'preco', 'categoria', 'editora', 'autores', 'capa')
        depth = 1


class LivroSerializer(serializers.ModelSerializer):
    capa_attachment_key = serializers.SlugRelatedField(
=======
        fields = '__all__'
        depth = 1
...
class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
>>>>>>> 289b2b8760bcde2e74635f8492ad2e3ddcee4bfd
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Livro
<<<<<<< HEAD
        fields = (
            'id', 'titulo', 'isbn', 'quantidade', 'preco',
            'categoria', 'editora', 'autores', 'capa', 'capa_attachment_key'
        )
=======
        fields = '__all__'
>>>>>>> 289b2b8760bcde2e74635f8492ad2e3ddcee4bfd
