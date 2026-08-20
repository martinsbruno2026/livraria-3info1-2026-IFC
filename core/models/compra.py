try:
    from django.db import models  # pyright: ignore[reportMissingImports]  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - fallback for static analysis / linters
    # Minimal stubs so linters/IDEs that can't import Django won't error.
    class _StubModels:
        class Model:  # base class for Django models
            pass

        # pylint: disable=invalid-name,unused-argument
        def ForeignKey(self, *_args, **_kwargs):
            return None

        def IntegerField(self, *_args, **_kwargs):
            return None

        CASCADE = None
        PROTECT = None

        class IntegerChoices:
            pass

    models = _StubModels()

from .livro import Livro
from .user import User


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        FINALIZADO = 2, 'Finalizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='+')
    quantidade = models.IntegerField(default=1)
