from django.db import models


class Categoria(models.Model):
    """Representa a categoria de um livro."""

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f'({self.id}) {self.descricao}'
