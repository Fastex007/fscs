from django.contrib import admin

from .models import Flight


class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'reg_number',
        'takeoff_airport',
        'landing_airport',
        'aircraft_commander',
        'first_officer',
        'aircraft',
        'flight_number',
        'flight_date',
        'takeoff_time',
        'landing_time',
        'qualification_exam',
        'copy_name',
        'process_duration',
        'landing_mode',
        'engine_monitoring',
    )
    search_fields = (
        'reg_number',
        'takeoff_airport',
        'landing_airport',
        'aircraft_commander',
        'first_officer',
        'aircraft',
        'flight_number',
        'flight_date',
        'takeoff_time',
        'landing_time',
        'qualification_exam',
        'copy_name',
        'process_duration',
        'landing_mode',
        'engine_monitoring',
    )
    list_filter = (
        'reg_number',
        'takeoff_airport',
        'landing_airport',
        'aircraft_commander',
        'first_officer',
        'aircraft',
        'flight_number',
        'flight_date',
        'takeoff_time',
        'landing_time',
        'qualification_exam',
        'copy_name',
        'process_duration',
        'landing_mode',
        'engine_monitoring',
    )
    empty_value_display = '-пусто-'


admin.site.register(Flight, FlightAdmin)


