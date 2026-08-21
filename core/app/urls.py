from rest_framework.routers import DefaultRouter

from .views import CategoriaViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet, basename="categorias")

from core.views import CategoriaViewSet, EditoraViewSet, UserViewSet

router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)