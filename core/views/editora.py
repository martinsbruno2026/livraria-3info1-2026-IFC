from rest_framework.viewsets import ModelViewSet
from core.models import Editora
from core.serializers import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora._default_manager.all()  # pylint: disable=no-member
    serializer_class = EditoraSerializer