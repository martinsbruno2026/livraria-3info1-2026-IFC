from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    @extend_schema(
        summary='Dados do usuário autenticado',
        description='Retorna os dados do usuário autenticado.',
        responses={200: UserSerializer, 401: None},
    )
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Retorna os dados do usuário autenticado."""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    class UserRegistrationView(ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserRegistrationSerializer  # noqa: F821
        permission_classes = [IsAuthenticated]
        http_method_names = ['post']

        @extend_schema(
            summary='Registrar novo usuário',
            description='Permite registrar um novo usuário.',
            request=UserRegistrationSerializer,  # noqa: F821
            responses={201: UserSerializer, 400: None},
        )
        def create(self, request, *args, **kwargs):
            """Registra um novo usuário."""
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
