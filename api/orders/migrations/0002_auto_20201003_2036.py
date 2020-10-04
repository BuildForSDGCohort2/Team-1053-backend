# Generated by Django 3.1 on 2020-10-03 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_delivery',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 7, 20, 36, 43, 937326), null=True),
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_item',
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(to='orders.OrderItem'),
        ),
    ]