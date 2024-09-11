"""
WSGI, or Web Server Gateway Interface, describes how a web server communicates with web applications;
The startproject command creates the wsgi.py file, containing our callable 'application';
WSGI servers will use this callable 'application' to communicate with the CD Spec code;
More information: https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/

Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
-------------
Comments pre-FA2022:
WSGI config for cd_spec_viewer_web project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cd_spec_viewer_web.settings")

application = get_wsgi_application()
