"""
WSGI config for django_socket project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_socket.settings")

from socketio import WSGIApp
from socketio_app.views import sio
django_app = get_wsgi_application()
application = WSGIApp(sio, django_app)

#
import eventlet
import eventlet.wsgi
eventlet.wsgi.server(eventlet.listen(('', 8000)), application)
