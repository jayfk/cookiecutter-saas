# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""

from .common import *  # noqa
import socket
import os

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='l7s34&gvw0^sg3t02_(w2p(g_%h56d6i!0ca!37b2x==9qu43-')

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_PORT = 1025
EMAIL_HOST = 'localhost'
CELERY_EMAIL_BACKEND = env('CELERY_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]
# tricks to have debug toolbar when developing with docker
if os.environ.get('USE_DOCKER') == 'yes':
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1]+"1"]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )
MEDIA_ROOT = str(APPS_DIR('media'))

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

<<<<<<< HEAD
PINAX_STRIPE_PUBLIC_KEY = ""
PINAX_STRIPE_SECRET_KEY = ""

OCTOBAT_IMAGE = "http://localhost:8000/static/images/logo_icon.png"

OCTOBAT_PUBLIC_KEY = ""
OCTOBAT_PRIVATE_KEY = ""
=======
PINAX_STRIPE_PUBLIC_KEY = "pk_test_q7jfeQ0vf3JdexuKiTqZmID0"
PINAX_STRIPE_SECRET_KEY = "sk_test_gq3Z8dtIdGYjxEcIrAPzNXh8"

OCTOBAT_IMAGE = "http://localhost:8000/static/images/logo_icon.png"

OCTOBAT_PUBLIC_KEY = "oc_test_pkey_9t5HOJXs2ocC0p1subuQIwtt"
OCTOBAT_PRIVATE_KEY = "oc_test_skey_aXjrKcBVUqdcsNYtH6YmWwtt"
>>>>>>> 3928c6bfe7fd05b36412501a53fc1e14383f218a

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

# Your local stuff: Below this line define 3rd party library settings
