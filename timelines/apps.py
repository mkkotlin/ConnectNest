from django.apps import AppConfig


class TimelinesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "timelines"

    def ready(self):
        import timelines.signals  # noqa: F401 — registers post_save signal
