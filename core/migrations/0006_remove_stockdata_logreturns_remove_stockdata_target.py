# Generated by Django 4.2.2 on 2023-06-29 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_stockdata_high_stockdata_low_stockdata_open_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdata',
            name='LogReturns',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='Target',
        ),
    ]