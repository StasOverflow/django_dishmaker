# Generated by Django 2.1.5 on 2019-02-13 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishmaker', '0006_auto_20190213_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishrecipe',
            name='description',
            field=models.TextField(blank=True, default='unset', null=True),
        ),
    ]