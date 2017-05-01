"""
WSGI config for doe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import django.core.handlers.wsgi

application = get_wsgi_application()


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doe.settings")

application = get_wsgi_application()
application = django.core.handlers.wsgi.WSGIHandler()
application = DjangoWhiteNoise(application)

# from dj_static import Cling
#
# application = Cling(get_wsgi_application())
