# -*- coding: utf-8 -*-
from django.apps import AppConfig

from health_check.plugins import plugin_dir


class HealthCheckConfig(AppConfig):
    name = 'health_check.contrib.sqs'

    def ready(self):
        from .backends import SQSHealthCheck
        plugin_dir.register(SQSHealthCheck)
