from django.conf import settings
from django.core.files.storage import FileSystemStorage


class VersionedMediaStorage(FileSystemStorage):
    """Append ?v=<MEDIA_VERSION> to media URLs.

    Bump MEDIA_VERSION in settings after replacing images in place so
    browsers fetch the new files instead of their cached copies.
    """

    def url(self, name):
        return f'{super().url(name)}?v={settings.MEDIA_VERSION}'
