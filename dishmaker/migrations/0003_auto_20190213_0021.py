# Generated by Django 2.1.5 on 2019-02-13 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishmaker', '0002_auto_20190212_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishrecipe',
            name='description',
            field=models.TextField(default='unset'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.TextField(default='unset'),
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
