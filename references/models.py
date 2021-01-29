from django.db import models

from lib.models import DateStamp
from lib.UpperCharField import UpperCharField


class AircraftType(DateStamp):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название типа ВС')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип воздушного судна'
        verbose_name_plural = 'Типы воздушных судов'


class Aircraft(DateStamp):
    type = models.ForeignKey(AircraftType, on_delete=models.PROTECT, related_name='types')
    registration_number = UpperCharField(max_length=10, unique=True, verbose_name='Регистрационный номер')

    def __str__(self):
        return f'{self.type} | {self.registration_number}'

    class Meta:
        verbose_name = 'Воздушное судно'
        verbose_name_plural = 'Воздушные суда'


class Airport(DateStamp):
    name = models.CharField(
        verbose_name='Название аэропорта',
        max_length=50,
        unique=True
    )
    icao_code = UpperCharField(
        verbose_name='ICAO код',
        max_length=4,
        unique=True
    )
    iata_code = UpperCharField(
        verbose_name='IATA код',
        max_length=4,
        unique=True
    )

    def __str__(self):
        return f'{self.iata_code} | {self.icao_code} | {self.name}'

    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'


class FlightSquad(DateStamp):
    name = models.CharField(
        verbose_name='Название лётного отряда',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return {self.name}

    class Meta:
        verbose_name = 'Лётный отряд'
        verbose_name_plural = 'Лётные отряды'
