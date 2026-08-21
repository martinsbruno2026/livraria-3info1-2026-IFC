from rest_framework.viewsets import ModelViewSet
from core.models import Categoria, Editora, Autor
from core.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ("descricao",)

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    search_fields = ("nome", "email", "cidade")

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ("nome", "email")
