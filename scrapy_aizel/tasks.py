from __future__ import absolute_import, unicode_literals
from celery import shared_task
from scrapy_aizel.models import AizelClothItem, Size


@shared_task
def items_transfer(items=None):
    for item in items:
        size_instance_list = list()
        for size in item['sizes']:
            instance, created = Size.objects.get_or_create(size_title=size)
            instance.save()
            size_instance_list.append(instance)

        cloth_item, exists = AizelClothItem.objects.get_or_create(
                            title=item['title'], brand=item['brand'], image=item['image'],
                            price=item['price'], descr=item['descr'], color=item['color']
                        )
        cloth_item.save()
        for size in size_instance_list:
            cloth_item.size.add(size)
