"""Creates a custom app for the users module

Prepared by COSC 401 as part of the CDSpec Viewer project for Dr. Sherrer

This file and all contributions herin are covered by the GPL 3.0 License 
https://www.gnu.org/licenses/gpl-3.0.html
"""
#commented by Andrew Kivrak
from django.apps import AppConfig #importing the module AppConfig from django.apps to configure the applications
from django.utils.translation import gettext_lazy as _ #translator


class UsersConfig(AppConfig): #UsersConfig is a subclass of the class 'AppConfig'
    name = 'users' #providing it a name as 'users'
    verbose_name = _("Users") #the human readable name

    def ready(self):
        #import the module cd_spec_viewer_web.users.signals -> if it is not present then the try block will throw an ImportError.
        try:
            import cd_spec_viewer_web.users.signals  # noqa F401
        except ImportError:
            pass
