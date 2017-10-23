# -*- coding: utf-8 -*-
import logging
import pika

from django.conf import settings

from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import ServiceUnavailable

class RMQHealthCheck(BaseHealthCheckBackend):
    def check_status(self):
        logger = logging.getLogger(__name__)
        try:
            pika.BlockingConnection(pika.ConnectionParameters(settings.HEALTH_CHECK_CONF['rmq_host']))
        except Exception, e:
            raise ServiceUnavailable("Connection Error")
