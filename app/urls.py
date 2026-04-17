import django.contrib
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, UserViewSet , EditoraViewSet , AutorViewSet , LivroViewSet

router = DefaultRouter()

router.register(r'categoria', CategoriaViewSet, basename='categorias')
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'editoras', EditoraViewSet, basename='editoras')
router.register(r'autores', AutorViewSet, basename='autores')
router.register(r'livros', LivroViewSet, basename='livros')

urlpatterns = [
    path('admin/', django.contrib.admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),

urlpatterns = [
    path('api/...', include(...)),
        path('api/media/', include(uploader_router.urls)),  
] 