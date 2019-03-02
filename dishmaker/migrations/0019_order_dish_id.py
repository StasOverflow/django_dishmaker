# Generated by Django 2.1.5 on 2019-03-02 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishmaker', '0018_order_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dish_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dish', to='dishmaker.Dish'),
        ),
    ]
