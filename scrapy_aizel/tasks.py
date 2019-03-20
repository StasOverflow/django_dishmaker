from __future__ import absolute_import, unicode_literals
from celery import shared_task
from dishmaker.celery import app
from dishmaker.models import Order
from django.utils import timezone


@shared_task
def multiply(x, y):
    return x*2 + y
