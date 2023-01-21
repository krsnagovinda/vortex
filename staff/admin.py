from django.contrib import admin
from .models import Staff

# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    fields= ['user','Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'Telefono', 'email', 'Foto']
    list_display = ['user', 'id','Nombre', 'Apellido_Paterno', 'Apellido_Materno']
    list_filter = []
    search_fields = ['id', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno']

admin.site.register(Staff, StaffAdmin)
