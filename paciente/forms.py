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
        fields =[
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

        widgets ={'Email': EmailInput(),
                  'Fecha_Nacimiento': DateInput(),}
        labels = {

            'id_Paciente' : 'Número Id de Paciente  ',
            'Nombre' : 'Nombre(s)  ',
            'Apellido_Paterno' : 'Apellido Paterno ',
            'Apellido_Materno' : 'Apellido Materno ',
            'Fecha_Nacimiento' : 'Fecha de Nacimiento (dd/mm/aaaa) ',
            'Edad' : 'Edad ',
            'Sexo' : 'Sexo ',
            'Ocupacion' : 'Ocupación:',
            'Domicilio' : 'Domicilio  ',
            'Ciudad' : 'Ciudad  ',
            'Telefono' : 'Teléfono o Celular  ',
            'Email' : 'E-mail:',
            'id_Expediente' : 'Numero de Ficha ',
            }

        required = True,
