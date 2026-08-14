from .autor import AutorViewSet
from .categoria import CategoriaViewSet
from .editora import EditoraViewSet
from .livro import LivroViewSet
from .user import UserRegistrationView, UserViewSet
from .compra import CompraViewSet

__all__ = [
    "AutorViewSet",
    "CategoriaViewSet",
    "EditoraViewSet",
    "LivroViewSet",
    "UserRegistrationView",
    "UserViewSet",
    "CompraViewSet",
]
