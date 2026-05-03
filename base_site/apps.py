from django.apps import AppConfig
from django.http import HttpResponse


class BaseSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_site'

