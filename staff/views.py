from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView

from .forms import StaffForm
from .models import Staff

def index(request):
    staff = Staff.objects.order_by(-id)
    contador = Staff.objects.all().count()

    context = {'staff':staff, 'contador':contador}

    return render(request, 'staff_lista.html', context)

# vistas CRUD de Medico
class StaffListView(ListView):
    model = Staff
    login_required = True
    template_name = 'staff_lista.html'
    context_object_name = 'staff'
    redirect_field_name = 'staff/staff_lista.html'

class UploadStaffView(CreateView):
    model = Staff
    login_required = True
    form_class = StaffForm
    success_url = reverse_lazy('class_staff_lista')
    template_name = 'upload_staff.html'

class StaffDetailView(DetailView):
    model = Staff
    login_required = True
    template_name = 'staff_detail.html'
    queryset = Staff.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Staff, id=id_)

class StaffUpdateView(UpdateView):
    model = Staff
    login_required = True
    template_name = 'staff_form.html'
    fields = [
              'user',
              'Nombre',
              'Apellido_Paterno',
              'Apellido_Materno',
              'Telefono',
              'email',
              'Foto',

              ]
    success_url = reverse_lazy('class_staff_lista')

class StaffDeleteView(DeleteView):
    model = Staff
    login_required = True
    template_name = 'staff_delete.html'
    success_url = reverse_lazy('class_staff_lista')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Staff, id=id_)
