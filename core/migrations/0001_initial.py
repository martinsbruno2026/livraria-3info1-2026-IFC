from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [("auth", "0012_alter_user_first_name_max_length")]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("is_superuser", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("foto", models.ImageField(blank=True, null=True, upload_to="usuarios/")),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("groups", models.ManyToManyField(blank=True, related_name="custom_user_set", related_query_name="custom_user", to="auth.group")),
                ("user_permissions", models.ManyToManyField(blank=True, related_name="custom_user_set", related_query_name="custom_user", to="auth.permission")),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Autor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Editora",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("site", models.URLField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                ("cidade", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Livro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=255)),
                ("isbn", models.CharField(blank=True, max_length=32, null=True)),
                ("quantidade", models.IntegerField(blank=True, default=0, null=True)),
                ("preco", models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ("capa", models.ImageField(blank=True, null=True, upload_to="livros/")),
                ("autores", models.ManyToManyField(blank=True, related_name="livros", to="core.autor")),
                ("categoria", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name="livros", to="core.categoria")),
                ("editora", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name="livros", to="core.editora")),
            ],
        ),
        migrations.CreateModel(
            name="Compra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.IntegerField(choices=[(1, "Carrinho"), (2, "Finalizado"), (3, "Pago"), (4, "Entregue")], default=1)),
                ("usuario", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="compras", to="core.user")),
            ],
        ),
        migrations.CreateModel(
            name="ItensCompra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantidade", models.IntegerField(default=1)),
                ("compra", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="itens", to="core.compra")),
                ("livro", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="+", to="core.livro")),
            ],
        ),
    ]
