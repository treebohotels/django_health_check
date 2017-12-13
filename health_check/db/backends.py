

from health_check.backends import BaseHealthCheckBackend


class DatabaseBackend(BaseHealthCheckBackend):

    def check_status(self):

        from health_check.exceptions import ServiceUnavailable
        from django.db import connections

        try:
            for db_conn_name in connections:
                connections[db_conn_name].cursor()
        except Exception:
            ServiceUnavailable("Database error")
