# Generated by Django 2.1.5 on 2019-03-02 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishmaker', '0019_order_dish_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
