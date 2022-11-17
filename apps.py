from django.apps import AppConfig


class {{ camel_case_app_name }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'singleton'

    def ready(self) -> None:

        try:
            # register any checks...
            import {{ app_name }}.checks  # noqa
        except ImportError:
            pass

        try:
            # register any signals...
            import {{ app_name }}.signals  # noqa
        except ImportError:
            pass
