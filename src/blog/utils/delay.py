from time import sleep

from django.conf import settings


def delay_middleware(get_response):
    """Adds fake loading delay to requests."""
    def middleware(request):
        response = get_response(request)

        if settings.DEBUG:
            sleep(getattr(settings, 'DELAY', 0))

        return response

    return middleware
