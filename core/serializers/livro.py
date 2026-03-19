from rest_framework import serializers
from core.models import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'  # ou liste os campos: ['id', 'titulo', 'isbn', 'quantidade', 'preco']