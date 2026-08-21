from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from core.views import (
    AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet,
    CompraViewSet, UserViewSet, RegistroView,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet, basename="categorias")
router.register(r"editoras", EditoraViewSet, basename="editoras")
router.register(r"autores", AutorViewSet, basename="autores")
router.register(r"livros", LivroViewSet, basename="livros")
router.register(r"compras", CompraViewSet, basename="compras")
router.register(r"usuarios", UserViewSet, basename="usuarios")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/registro/", RegistroView.as_view(), name="registro"),
    path("api/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
