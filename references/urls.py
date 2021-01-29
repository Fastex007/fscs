from django.urls import path

from . import views


app_name = 'references'


urlpatterns = [
    path('aircraft_types/',
         views.AircraftTypesList.as_view(),
         name='aircraft_types_list'),

    path('aircraft_types/add/', views.AircraftTypeCreate.as_view(), name='add_aircraft_type'),

    path('aircrafts/',
         views.AircraftsList.as_view(),
         name='aircrafts_list'),

    path('airports/',
         views.AirportsList.as_view(),
         name='airports_list'),
]
