# Generated by Django 3.1.4 on 2020-12-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_date',
            field=models.DateField(verbose_name='Дата полёта'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='landing_time',
            field=models.TimeField(verbose_name='Время посадки'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='process_duration',
            field=models.TimeField(verbose_name='Продолжительность обработки'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='takeoff_time',
            field=models.TimeField(verbose_name='Время взлёта'),
        ),
    ]