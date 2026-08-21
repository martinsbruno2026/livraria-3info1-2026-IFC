import mimetypes
import uuid
from typing import Any

try:
    from django.db import models
except ImportError:  # pragma: no cover

    class _MissingDjangoModel:
        pass

    class _MissingDjangoField:
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            pass

    class _MissingDjangoModels:
        Model = _MissingDjangoModel
        UUIDField = _MissingDjangoField
        ImageField = _MissingDjangoField
        CharField = _MissingDjangoField
        DateTimeField = _MissingDjangoField

    models = _MissingDjangoModels()


def image_file_path(image, _) -> str:
    content_type = getattr(getattr(image.file, 'file', None), 'content_type', None)
    extension = mimetypes.guess_extension(content_type or '') or ''
    if extension == '.jpe':
        extension = '.jpg'
    return f'images/{image.public_id}{extension}'


class Image(models.Model):
    attachment_key = models.UUIDField(
        max_length=255,
        default=uuid.uuid4,
        unique=True,
        help_text=('Used to attach the image to another object. Cannot be used to retrieve the image file.'),
    )
    public_id = models.UUIDField(
        max_length=255,
        default=uuid.uuid4,
        unique=True,
        help_text=(
            'Used to retrieve the image itself. Should not be readable until the image is attached to another object.'
        ),
    )
    file = models.ImageField(upload_to=image_file_path)
    description = models.CharField(max_length=255, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.description} - {self.attachment_key}'

    @property
    def url(self) -> str:
        return self.file.url  # pylint: disable=no-member
