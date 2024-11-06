from django.apps import AppConfig

class DuckFumAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DuckFumApp'  # Este nombre debe coincidir con el nombre de la aplicación en INSTALLED_APPS