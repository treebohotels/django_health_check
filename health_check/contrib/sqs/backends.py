# -*- coding: utf-8 -*-
import logging
from django.conf import settings
from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import ServiceUnavailable
import boto3


class SQSHealthCheck(BaseHealthCheckBackend):
    logger = logging.getLogger(__name__)

    def check_status(self):
        try:
            sqs = boto3.resource('sqs',
                                 region_name=settings.HEALTH_CHECK_CONF['region_name'],
                                 aws_secret_access_key=settings.HEALTH_CHECK_CONF['aws_secret_access_key'],
                                 aws_access_key_id=settings.HEALTH_CHECK_CONF['aws_access_key_id']
                                 )
            q = sqs.get_queue_by_name(QueueName=settings.HEALTH_CHECK_CONF['sqs_queue_name'])
        except Exception, e:
            raise ServiceUnavailable("connection error")

