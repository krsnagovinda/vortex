from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView, FormView

from .forms import PacienteForm, RecordForm
from .models import Record, Paciente


# Create your views here.

def index(request):
    pacientes = Paciente.objects.order_by('-id')
    paginator = Paginator(pacientes,10)
    contador = Paciente.objects.all().count()
    hombres_contador = Paciente.objects.filter(Sexo__contains='M').count()
    mujeres_contador = Paciente.objects.filter(Sexo__contains='F').count()
    mayores_80 = Paciente.objects.filter(Edad__gte=80).count()
    pacientes_10 = Paciente.objects.filter(Edad__lte=10).count()


    page = request.GET.get('page')
    paged_pacientes = paginator.get_page(page)

    context = {'pacientes' : paged_pacientes, 'contador':contador,
               'hombres_contador':hombres_contador, 'mujeres_contador':mujeres_contador,
               'mayores_80':mayores_80, 'pacientes_10':pacientes_10,
               }

    return render (request, 'pacientes_lista.html', context)



class SearchResultsView(ListView):
    model = Paciente
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paciente.objects.filter(
            Q(id_Paciente__icontains=query) | Q(Nombre__icontains=query) | Q(Apellido_Paterno__icontains=query)
        )
        return object_list

# vistas CRUD de Paciente


class UploadPacienteView(CreateView):
    model = Paciente
    login_required = True
    form_class = PacienteForm
    success_url = reverse_lazy('class_pacientes_lista')
    template_name = 'upload_paciente.html'
    success_message = "Paciente registrado correctamente"

class PacienteDetailView(DetailView):
    model = Paciente
    login_required = True
    template_name = 'paciente_detail.html'
    queryset = Paciente.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Paciente, id=id_)

class PacienteUpdateView(UpdateView):
    model = Paciente
    login_required = True
    template_name = 'paciente_form.html'
    fields = [
              'id_Expediente',
              'id_Paciente',
              'Nombre',
              'Apellido_Paterno',
              'Apellido_Materno',
              'Fecha_Nacimiento',
              'Edad',
              'Sexo',
              'Estado_Civil',
              'Ocupacion',
              'Nacionalidad',
              'Domicilio',
              'Ciudad',
              'Telefono',
              'Email',
            ]
    success_url = reverse_lazy('class_pacientes_lista')

#   vistas CRUD de Record
class UploadRecordView(CreateView):
    model = Record
    login_required = True
    form_class = RecordForm
    success_url = reverse_lazy('class_upload_paciente')
    template_name = 'upload_record.html'

class RecordDetailView(DetailView):
    model = Record
    login_required = True
    template_name = 'record_detail.html'
    queryset = Record.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Record, id=id_)

class RecordUpdateView(UpdateView):
    model = Record
    login_required = True
    template_name = 'record_form.html'
    fields = ['id_record',
              'Expediente',
            ]
    success_url = reverse_lazy('class_pacientes_lista')

class RecordDeleteView(DeleteView):
    model = Record
    login_required = True
    template_name = 'paciente_delete.html'
    success_url = reverse_lazy('class_pacientes_lista')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Record, id=id_)
