"""
ASGI config for writers_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# TODO: Change this in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "writers_api.settings.local")

application = get_asgi_application()
