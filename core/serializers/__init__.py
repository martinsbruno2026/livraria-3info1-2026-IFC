import sys

from . import catalogo
from .catalogo import AutorSerializer, CategoriaSerializer, EditoraSerializer
from .compra import CompraSerializer, ItensCompraSerializer
from .livro import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer
from .user import UserRegistrationSerializer, UserSerializer

# Backwards-compatible alias for imports using the old module name
sys.modules.setdefault(f"{__name__}.categoria", catalogo)
