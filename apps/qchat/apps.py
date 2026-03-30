from django.apps import AppConfig


class QchatConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"

    name = "apps.qchat"

    def ready(self):
        import apps.qchat.signals
