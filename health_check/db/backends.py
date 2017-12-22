

from health_check.backends import BaseHealthCheckBackend


class DatabaseBackend(BaseHealthCheckBackend):

    def check_status(self):

        from health_check.exceptions import ServiceUnavailable
        from django.db import connections

        try:
            for db_conn_name in connections:
                with connections[db_conn_name].cursor() as c:
                    c.execute('select 1;')
                    c.fetchall()
        except Exception:
            ServiceUnavailable("Database error")
