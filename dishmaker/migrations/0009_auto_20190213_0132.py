# Generated by Django 2.1.5 on 2019-02-13 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishmaker', '0008_auto_20190213_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishrecipe',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
