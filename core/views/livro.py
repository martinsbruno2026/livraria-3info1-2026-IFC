from rest_framework.viewsets import ModelViewSet
from core.models import Livro
from core.serializers import LivroSerializer, LivroListSerializer, LivroRetrieveSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.select_related("categoria", "editora").prefetch_related("autores").all()
    serializer_class = LivroSerializer
    search_fields = ("titulo", "isbn")
    ordering_fields = ("titulo", "preco", "quantidade")

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        if self.action == "retrieve":
            return LivroRetrieveSerializer
        return LivroSerializer
