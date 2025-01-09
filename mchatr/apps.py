from django.apps import AppConfig


class MchatrConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mchatr"
    def ready(self) -> None:
        import mchatr.signals
