# Generated by Django 3.1.4 on 2020-12-29 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('references', '0002_auto_20201229_1746'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('edited_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено')),
                ('reg_number', models.CharField(max_length=7, verbose_name='Регистрационный номер по журналу учёта')),
                ('flight_number', models.CharField(max_length=10, verbose_name='Номер рейса')),
                ('flight_date', models.DateTimeField(verbose_name='Дата полёта')),
                ('takeoff_time', models.DateTimeField(verbose_name='Время взлёта')),
                ('landing_time', models.DateTimeField(verbose_name='Время посадки')),
                ('qualification_exam', models.BooleanField(verbose_name='Квалификационная проверка')),
                ('copy_name', models.CharField(max_length=255, verbose_name='Файл копии ПИ')),
                ('process_duration', models.DurationField(verbose_name='Продолжительность обработки')),
                ('landing_mode', models.CharField(choices=[('Инструментальный', 'Инструментальный'), ('Визуальный', 'Визуальный'), ('Автоматический', 'Автоматический')], max_length=20, verbose_name='Режим посадки')),
                ('engine_monitoring', models.BooleanField(verbose_name='Мониторинг двигателей')),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aircraft', to='references.aircraft')),
                ('aircraft_commander', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aircraft_commander', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создал')),
                ('edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='flight_editor', to=settings.AUTH_USER_MODEL, verbose_name='Изменил')),
                ('first_officer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='first_officer', to=settings.AUTH_USER_MODEL)),
                ('landing_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='landing_airport', to='references.airport')),
                ('takeoff_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='takeoff_airport', to='references.airport')),
            ],
            options={
                'verbose_name': 'Полёт',
                'verbose_name_plural': 'Полёты',
            },
        ),
    ]