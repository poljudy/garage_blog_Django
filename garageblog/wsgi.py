"""
WSGI config for garageblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# was successfully able to change the Django site name to garageblog early on
# in Heroku and here
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'garageblog.settings')

application = get_wsgi_application()
