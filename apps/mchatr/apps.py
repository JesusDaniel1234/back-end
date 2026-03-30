from django.apps import AppConfig


class MchatrConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"

    name = "apps.mchatr"

    def ready(self) -> None:
        import apps.mchatr.signals
