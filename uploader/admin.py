try:
    from django.contrib import admin
except (
    ImportError,
    ModuleNotFoundError,
):  # pragma: no cover - provide lightweight fallback for linters/environments without Django

    class _DummyModelAdmin:
        pass

    class _DummySite:
        def register(self, *args, **kwargs):
            return None

    admin = type('admin', (), {'ModelAdmin': _DummyModelAdmin, 'site': _DummySite()})


# Use relative import to avoid import resolution issues in some environments
from .models import Document, Image


class ImageAdmin(admin.ModelAdmin):
    pass


class DocumentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)
admin.site.register(Document, DocumentAdmin)
