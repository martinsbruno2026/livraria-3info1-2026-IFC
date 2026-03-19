# livraria/views/livro_view.py
from rest_framework import viewsets
from core.models import Livro
from core.serializers.livro import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    # filterset_fields = ['titulo', 'isbn']           # opcional
    # search_fields = ['titulo', 'isbn']               # opcional
    # ordering_fields = ['titulo', 'preco']            # opcional