from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from .models import AircraftType, Aircraft, Airport
from .forms import AircraftTypeForm


# Отображаем список типов возудных судов
class AircraftTypesList(LoginRequiredMixin, ListView):
    template_name = 'aircraft_types/aircraft_types_list.html'
    queryset = AircraftType.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AircraftTypesList, self).get_context_data(**kwargs)
        context['model_caption'] = AircraftType._meta.verbose_name_plural
        context['ac_types'] = AircraftType.objects.all()
        return context


# Добавляем новый тип воздушного судна
class AircraftTypeCreate(LoginRequiredMixin, CreateView):
    form_class = AircraftTypeForm
    success_url = '/references/aircraft_types'
    template_name = 'aircraft_types/add_aircraft_type.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# Отображаем список возудных судов
class AircraftsList(LoginRequiredMixin, ListView):
    template_name = 'aircrafts/aircrafts_list.html'
    queryset = Aircraft.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AircraftsList, self).get_context_data(**kwargs)
        context['model_caption'] = Aircraft._meta.verbose_name_plural
        context['aircrafts'] = Aircraft.objects.all()
        return context


# Отображаем список аэропортов
class AirportsList(LoginRequiredMixin, ListView):
    template_name = 'airports/airports_list.html'
    queryset = Airport.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AirportsList, self).get_context_data(**kwargs)
        context['model_caption'] = Airport._meta.verbose_name_plural
        context['airports'] = Airport.objects.all()
        return context
