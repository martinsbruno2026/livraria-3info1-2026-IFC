from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .livro import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer
from .user import UserRegistrationSerializer, UserSerializer
from .compra import CompraSerializer

__all__ = [
	"AutorSerializer",
	"CategoriaSerializer",
	"EditoraSerializer",
	"LivroListSerializer",
	"LivroRetrieveSerializer",
	"LivroSerializer",
	"UserRegistrationSerializer",
	"UserSerializer",
	"CompraSerializer",
]
