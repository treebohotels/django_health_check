from django.db import connections
from django.db.utils import OperationalError

from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import ServiceUnavailable


class DatabaseBackend(BaseHealthCheckBackend):

    def check_status(self):

        try:
            for db_conn in connections:
                db_conn.cursor()
        except OperationalError:
            ServiceUnavailable("Database error")
