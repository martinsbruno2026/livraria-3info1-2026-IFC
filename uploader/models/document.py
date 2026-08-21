import mimetypes
import uuid

try:
    from django.db import models  # pyright: ignore[reportMissingImports, reportMissingModuleSource]
except ImportError:  # pragma: no cover - only for environments without Django available at analysis time.

    class _FallbackModel:  # type: ignore[no-redef]
        pass

    class _FallbackField:  # type: ignore[no-redef]
        def __init__(self, *args, **kwargs):
            pass

    class _FallbackUUIDField(_FallbackField):
        pass

    class _FallbackFileField(_FallbackField):
        pass

    class _FallbackCharField(_FallbackField):
        pass

    class _FallbackDateTimeField(_FallbackField):
        pass

    class models:  # type: ignore[no-redef]
        Model = _FallbackModel
        UUIDField = _FallbackUUIDField
        FileField = _FallbackFileField
        CharField = _FallbackCharField
        DateTimeField = _FallbackDateTimeField


from uploader.helpers.files import get_content_type


def document_file_path(document, _) -> str:
    content_type = get_content_type(document.file)
    extension: str = mimetypes.guess_extension(content_type)

    return f'documents/{document.public_id}{extension or ""}'


class Document(models.Model):
    attachment_key = models.UUIDField(
        max_length=255,
        default=uuid.uuid4,
        unique=True,
        help_text=('Used to attach the document to another object. Cannot be used to retrieve the document file.'),
    )
    public_id = models.UUIDField(
        max_length=255,
        default=uuid.uuid4,
        unique=True,
        help_text=(
            'Used to retrieve the document file itself. '
            'Should not be readable until the document is attached to another object.'
        ),
    )
    file = models.FileField(upload_to=document_file_path)
    description = models.CharField(max_length=255, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.description} - {self.file.name}'

    @property
    def url(self) -> str:
        return self.file.url  # pylint: disable=no-member
