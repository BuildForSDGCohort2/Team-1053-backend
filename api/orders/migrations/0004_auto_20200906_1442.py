# Generated by Django 3.1 on 2020-09-06 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200906_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]