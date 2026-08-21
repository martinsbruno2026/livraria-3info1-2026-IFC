from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria._default_manager.all()  # pylint: disable=no-member
    serializer_class = CategoriaSerializer
