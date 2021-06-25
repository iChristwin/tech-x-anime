from django.apps import AppConfig


class RowsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rowsite'

    def ready(self):
        import rowsite.signals
