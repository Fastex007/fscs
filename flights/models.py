from django.db import models

from lib.models import DateStamp, user
from references.models import Airport, Aircraft


class Flight(DateStamp):
    reg_number = models.CharField(
        verbose_name='Регистрационный номер по журналу учёта',
        max_length=7,
        unique=False,
        null=False
    )
    takeoff_airport = models.ForeignKey(
        Airport,
        on_delete=models.PROTECT,
        related_name='takeoff_airport'
    )
    landing_airport = models.ForeignKey(
        Airport,
        on_delete=models.PROTECT,
        related_name='landing_airport'
    )
    aircraft_commander = models.ForeignKey(
        user,
        on_delete=models.PROTECT,
        related_name='aircraft_commander'
    )
    first_officer = models.ForeignKey(
        user,
        on_delete=models.PROTECT,
        related_name='first_officer'
    )
    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.PROTECT,
        related_name='aircraft'
    )
    flight_number = models.CharField(
        verbose_name='Номер рейса',
        max_length=10,
        unique=False,
        null=False
    )
    flight_date = models.DateField(verbose_name='Дата полёта')
    takeoff_time = models.TimeField(verbose_name='Время взлёта')
    landing_time = models.TimeField(verbose_name='Время посадки')
    qualification_exam = models.BooleanField(verbose_name='Квалификационная проверка')
    copy_name = models.CharField(verbose_name='Файл копии ПИ', max_length=255)
    # process_interval =
    process_duration = models.TimeField(verbose_name='Продолжительность обработки')
    LANDING_MODE_CHOICES = [
        ('Инструментальный', 'Инструментальный'),
        ('Визуальный', 'Визуальный'),
        ('Автоматический', 'Автоматический')
    ]
    landing_mode = models.CharField(verbose_name='Режим посадки',
                                    max_length=20,
                                    choices=LANDING_MODE_CHOICES)
    engine_monitoring = models.BooleanField(verbose_name='Мониторинг двигателей')

    def __str__(self):
        return f'{self.flight_number} | {self.flight_date} | {self.aircraft}'

    class Meta:
        verbose_name = 'Полёт'
        verbose_name_plural = 'Полёты'
