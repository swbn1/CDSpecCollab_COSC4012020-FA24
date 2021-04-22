from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = _("Users")

    def ready(self):
        try:
            import cd_spec_viewer_web.users.signals  # noqa F401
        except ImportError:
            pass