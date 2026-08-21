from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, display, register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User, Autor, Categoria, Editora, Livro, Compra, ItensCompra

@register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ("email",)
    list_display = ("email", "name", "is_staff", "is_active")
    search_fields = ("email", "name")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações", {"fields": ("name", "foto")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "name", "password1", "password2", "is_staff", "is_superuser")}),
    )

@register(Autor)
class AutorAdmin(ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome", "email")
    ordering = ("nome",)

@register(Categoria)
class CategoriaAdmin(ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    ordering = ("descricao",)

@register(Editora)
class EditoraAdmin(ModelAdmin):
    list_display = ("nome", "email", "cidade")
    search_fields = ("nome", "email", "cidade")
    ordering = ("nome",)

@register(Livro)
class LivroAdmin(ModelAdmin):
    list_display = ("titulo", "editora", "categoria", "preco", "quantidade")
    search_fields = ("titulo", "editora__nome", "categoria__descricao")
    list_filter = ("editora", "categoria")
    ordering = ("titulo",)
    filter_horizontal = ("autores",)

class ItensCompraInline(TabularInline):
    model = ItensCompra
    extra = 1

@register(Compra)
class CompraAdmin(ModelAdmin):
    list_display = ("usuario", "status", "total_formatado")
    ordering = ("usuario", "status")
    inlines = [ItensCompraInline]
    readonly_fields = ("total_formatado",)

    @display(description="Total")
    def total_formatado(self, obj):
        return f"R$ {obj.total:.2f}"
