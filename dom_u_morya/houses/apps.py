from django.apps import AppConfig


class HousesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'houses'

    verbose_name = 'Дом'
    verbose_name_plural = 'Дома'
