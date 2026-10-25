from django.conf import settings
from whitenoise.middleware import WhiteNoiseMiddleware


class MediaWhiteNoiseMiddleware(WhiteNoiseMiddleware):
    """Serve uploaded media files with WhiteNoise as well as static files.

    Without this, /media/ is served by Django's slow debug file view with no
    caching headers.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)

