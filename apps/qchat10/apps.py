from django.apps import AppConfig


class Qchat10Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.qchat10"
    
    def ready(self) -> None:
        import apps.qchat10.signals
