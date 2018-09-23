from django.core.management.base import BaseCommand, CommandError
from hydro.models import *

import logging
from django.utils import timezone

log = logging.getLogger('hydro')


class Command(BaseCommand):
    help = 'Configures models for the argue application.'

    def handle(self, *args, **options):
        """Adds default entries for the argue app.
            :returns: None
            """

    log.info("Configuration complete")
