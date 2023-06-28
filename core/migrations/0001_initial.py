# Generated by Django 4.2.2 on 2023-06-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Close', models.FloatField()),
                ('LogReturns', models.FloatField()),
                ('Target', models.FloatField()),
            ],
        ),
    ]