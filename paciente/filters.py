from django.contrib.auth.models import User
import django_filters
from . models import Paciente, Record


class PacienteFilter(django_filters.FilterSet):
        Nombre = django_filters.CharFilter(lookup_expr='icontains')

        class Meta:
            model = Paciente
            fields = ('Nombre', 'Apellido_Paterno', 'Apellido_Materno')
