try:
    from django.apps import AppConfig
except ImportError:  # pragma: no cover

    class AppConfig:  # type: ignore[no-redef]
        pass


class MediaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uploader'
