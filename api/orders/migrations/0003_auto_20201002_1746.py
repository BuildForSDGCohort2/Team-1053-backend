# Generated by Django 3.1 on 2020-10-02 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201002_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_delivery',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 6, 17, 46, 21, 693236), null=True),
        ),
    ]
