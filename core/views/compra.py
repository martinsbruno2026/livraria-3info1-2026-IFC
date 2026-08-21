from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import Compra
from core.serializers import CompraSerializer

class CompraViewSet(ModelViewSet):
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Compra.objects.filter(usuario=self.request.user).prefetch_related("itens__livro")

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
