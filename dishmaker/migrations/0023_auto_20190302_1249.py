# Generated by Django 2.1.5 on 2019-03-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishmaker', '0022_auto_20190302_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
