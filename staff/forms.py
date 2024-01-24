from django.forms import ModelForm, Textarea, EmailInput, DateInput
from . models import Staff
from django import forms
from decimal import Decimal, DecimalException

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'Telefono', 'email', 'Foto']
        widgets ={
                 }

        labels = {

            'Nombre' : 'Nombre del Usuario',
                }
        required = True,
