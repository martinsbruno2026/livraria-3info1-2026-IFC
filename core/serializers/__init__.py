from .catalogo import CategoriaSerializer, EditoraSerializer, AutorSerializer
from .livro import LivroSerializer, LivroListSerializer, LivroRetrieveSerializer
from .user import UserSerializer, UserRegistrationSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraSerializer,
)
