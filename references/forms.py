from django.forms import ModelForm

from .models import AircraftType


class AircraftTypeForm(ModelForm):

    class Meta:
        model = AircraftType
        fields = ['name']
        help_texts = {'name': 'Название типа воздушного судна'}
