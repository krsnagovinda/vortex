from django.contrib import admin
from .models import Paciente, Record

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    fields =['id_Paciente', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'Fecha_Nacimiento', 'Edad', 'Sexo', 'Estado_Civil', 'Ocupacion', 'Nacionalidad', 'Domicilio', 'Ciudad', 'Telefono', 'Email', 'Foto', 'id_Expediente']
    list_display =['id_Paciente', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno']
    list_filter =[]
    search_fields =['id_Paciente', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno']

class RecordAdmin(admin.ModelAdmin):
    fields= ['id_record', 'Expediente']
    list_display = ['id_record']
    list_filter = []
    search_fields = ['id_record', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno']

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Record, RecordAdmin)