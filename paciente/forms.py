from django.forms import ModelForm, Textarea, EmailInput, DateInput
from . models import Paciente, Record
from django import forms
from decimal import Decimal, DecimalException
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['id_record','Expediente']
        widgets ={'Expediente': forms.CharField(widget=CKEditorUploadingWidget()),
                 }

        labels = {
            'id_record' : 'Número de Ficha Clínica ',
            'Expediente' : 'Observaciones de Expediente ',
                }
        required = True,


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['id_Expediente',
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
            'Email',]
        required = True,

     
