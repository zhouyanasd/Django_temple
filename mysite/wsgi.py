"""
WSGI config for feco project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()

import sys
sys.path.append('C:/Users/Administrator/PycharmProjects/lyapi')

# import os
# import sys
#
# #添加setting文件地址
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# #添加项目路径到sys.path
# sys.path.append('C:\Users\Administrator\PycharmProjects\lyapi\mysite')
# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()