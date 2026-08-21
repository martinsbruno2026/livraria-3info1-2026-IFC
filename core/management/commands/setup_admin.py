from django.core.management.base import BaseCommand
from core.models import User


class Command(BaseCommand):
    help = "Cria ou atualiza o superusuário padrão do projeto."

    def handle(self, *args, **options):
        email = "a@a.com"
        password = "teste.123"

        user, created = User.objects.get_or_create(
            email=email,
            defaults={"name": "Administrador"},
        )
        user.name = user.name or "Administrador"
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        action = "criado" if created else "atualizado"
        self.stdout.write(
            self.style.SUCCESS(
                f"Superusuário {action}: {email} / {password}"
            )
        )
