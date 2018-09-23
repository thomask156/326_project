from django.apps import AppConfig
import django.utils.timezone as tz
import logging


log = logging.getLogger('argue')

class ArgueConfig(AppConfig):
    name = 'argue'
    verbose_name = 'Argue Application'

    def ready(self):
        pass