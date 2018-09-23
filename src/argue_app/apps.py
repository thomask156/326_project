from django.apps import AppConfig
import django.utils.timezone as tz
import threading
from subprocess import PIPE
import subprocess
import datetime
import time
import logging


log = logging.getLogger('argue')

class ArgueConfig(AppConfig):
    name = 'argue'
    verbose_name = 'Argue Application'

    def ready(self):
        pass