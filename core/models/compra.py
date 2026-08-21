from django.db import models
from .user import User
from .livro import Livro

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        FINALIZADO = 2, "Finalizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)

    @property
    def total(self):
        return sum(item.livro.preco * item.quantidade for item in self.itens.select_related("livro").all())

    def __str__(self):
        return f"Compra #{self.id} - {self.usuario.email}"

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)

    @property
    def total(self):
        return self.livro.preco * self.quantidade

    def __str__(self):
        return f"{self.livro.titulo} x {self.quantidade}"
