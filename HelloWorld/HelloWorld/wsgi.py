"""
WSGI config for HelloWorld project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/

用于HeloWord项目的WSGi配置。
它将WSGI作为模块级变量调用，称为“应用程序”。
有关此文件的更多信息，请参见
HTTPS://DOCS.djangojtup.COM/En/2.1/Hoto/AdvestMy/WSGI/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HelloWorld.settings')

application = get_wsgi_application()
