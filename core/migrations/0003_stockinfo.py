# Generated by Django 4.2.2 on 2023-06-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_stockdata_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
    ]
