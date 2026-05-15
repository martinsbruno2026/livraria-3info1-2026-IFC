try:
    from drf_spectacular.utils import extend_schema  # pylint: disable=import-error
except ImportError:
    def extend_schema(*args, **kwargs):
        def decorator(func):
            return func
        return decorator

try:
    from rest_framework import status
    from rest_framework.decorators import action
    from rest_framework.generics import CreateAPIView
    from rest_framework.permissions import AllowAny, IsAuthenticated
    from rest_framework.response import Response
    from rest_framework.viewsets import ModelViewSet  # pylint: disable=import-error
except ImportError:
    class Status:
        HTTP_200_OK = 200

    status = Status()

    def action(*_args, **_kwargs):
        def decorator(func):
            return func
        return decorator

    class CreateAPIView:
        pass

    class AllowAny:
        pass

    class IsAuthenticated:
        pass

    class Response:
        def __init__(self, data=None, status=None):
            self.data = data
            self.status = status

    class ModelViewSet:
        def get_permissions(self):
            return []

from core.models import User
from core.serializers import (
    UserRegistrationSerializer,
    UserSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """Define permissões dinâmicas: 'me' precisa de login, 'create' é aberto."""
        if self.action == 'me':
            return [IsAuthenticated()]
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        """Usa o serializer de registro ao criar um usuário."""
        if self.action == 'create':
            return UserRegistrationSerializer
        return UserSerializer

    @extend_schema(
        summary="Dados do usuário autenticado",
        description="Retorna os dados do usuário autenticado.",
        responses={200: UserSerializer, 401: None},
    )
    @action(detail=False, methods=['get'])
    def me(self, request):
        """ Retorna os dados do usuário autenticado."""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegistrationView(CreateAPIView):
    """Endpoint para registro de novos usuários."""

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
