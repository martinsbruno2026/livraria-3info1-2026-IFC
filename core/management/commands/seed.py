from django.core.management.base import BaseCommand
from core.models import Categoria, Editora, Autor, Livro

class Command(BaseCommand):
    help = "Cria dados iniciais para testar a Livraria."

    def handle(self, *args, **options):
        categorias = ["Ficção", "Tecnologia", "Fantasia", "Romance"]
        for descricao in categorias:
            Categoria.objects.get_or_create(descricao=descricao)

        editoras = [
            ("Editora Exemplo", "https://example.com", "contato@example.com", "São Paulo"),
            ("Editora Tech", "https://example.com", "tech@example.com", "Florianópolis"),
        ]
        for nome, site, email, cidade in editoras:
            Editora.objects.get_or_create(nome=nome, defaults={
                "site": site, "email": email, "cidade": cidade
            })

        autores = [
            ("Autor Exemplo", "autor@example.com"),
            ("Autor Tech", "tech@example.com"),
        ]
        for nome, email in autores:
            Autor.objects.get_or_create(nome=nome, defaults={"email": email})

        categoria = Categoria.objects.first()
        editora = Editora.objects.first()
        autor = Autor.objects.first()
        if not Livro.objects.exists():
            livro = Livro.objects.create(
                titulo="Livro de Exemplo",
                isbn="9780000000000",
                quantidade=10,
                preco="49.90",
                categoria=categoria,
                editora=editora,
            )
            livro.autores.add(autor)

        self.stdout.write(self.style.SUCCESS("Dados iniciais criados."))
