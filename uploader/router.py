from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rest_framework.routers import DefaultRouter
else:
    try:
        from rest_framework.routers import DefaultRouter
    except ImportError:
        DefaultRouter = None

from uploader import views

app_name = 'uploader'

router = DefaultRouter()
router.register('images', views.ImageUploadViewSet)
router.register('documents', views.DocumentUploadViewSet)
