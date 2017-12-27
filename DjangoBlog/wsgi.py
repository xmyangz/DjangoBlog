"""
WSGI config for DjangoBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoBlog.settings")

application = Cling(get_wsgi_application())
#application = get_wsgi_application()

''' for Debug
if sys.platform == 'darwin': #mac本机
	from wdb.ext import WdbMiddleware
	application = WdbMiddleware(application)
'''