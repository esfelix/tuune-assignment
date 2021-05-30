from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IncomeTaxConfig(AppConfig):
    name = "apps.income_tax"
    verbose_name = _("IncomeTax")

    def ready(self):
        try:
            import apps.users.signals  # noqa F401
        except ImportError:
            pass
