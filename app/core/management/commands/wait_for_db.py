"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from typing import Any, Optional
import time


class Command(BaseCommand):
    """django commnad to wait database"""

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write("waiting for database...")

        db_up: bool = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Databases unavailable, waiting 1 seconds.")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
