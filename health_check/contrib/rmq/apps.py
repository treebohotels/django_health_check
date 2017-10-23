# -*- coding: utf-8 -*-
from django.apps import AppConfig

from health_check.plugins import plugin_dir


class HealthCheckConfig(AppConfig):
    name = 'health_check.contrib.rmq'

    def ready(self):
        from .backends import RMQHealthCheck
        plugin_dir.register(RMQHealthCheck)
