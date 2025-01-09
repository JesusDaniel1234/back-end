from django.apps import AppConfig


class Qchat10Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "qchat10"
    
    def ready(self) -> None:
        import qchat10.signals
