from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .celery import app
from dishmaker.models import Order
from django.utils import timezone


@shared_task
def add(x, y):
    return x + y


@app.task
def flag_expired_order(*args, **kwargs):
    orders = Order.objects.all()
    for order in orders:
        if order.is_active:
            if (order.created_on + timezone.timedelta(seconds=80)) <= timezone.now():
                order.is_active = False
                order.save()
