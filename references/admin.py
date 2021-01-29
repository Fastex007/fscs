from django.contrib import admin

from .models import AircraftType, Aircraft, Airport, FlightSquad


class AircraftTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class AircraftAdmin(admin.ModelAdmin):
    list_display = ('pk', 'registration_number',)
    search_fields = ('registration_number',)
    list_filter = ('registration_number',)
    empty_value_display = '-пусто-'


class AirportAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'icao_code',
        'iata_code',
    )
    search_fields = (
        'name',
        'icao_code',
        'iata_code',
    )
    list_filter = (
        'name',
        'icao_code',
        'iata_code',
    )
    empty_value_display = '-пусто-'


class FlightSquadAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )
    empty_value_display = '-пусто-'


admin.site.register(AircraftType, AircraftTypeAdmin)
admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(FlightSquad, FlightSquadAdmin)
