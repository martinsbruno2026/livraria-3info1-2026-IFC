from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from core.models import User
from core.serializers import UserSerializer, UserRegistrationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

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
        summary='Dados do usuário autenticado',
        description='Retorna os dados do perfil do usuário logado via Token/JWT.',
        responses={200: UserSerializer, 401: None},
    )
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Endpoint: /users/me/"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


