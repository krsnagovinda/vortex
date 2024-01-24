from django.db import models
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Record(models.Model):
    id_record = models.CharField(max_length=50, null=True, unique=True)
    Expediente = RichTextUploadingField()

    def __str__(self):
        return str(self.id_record)

class Paciente(models.Model):
    sexo_opciones= (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    id_Paciente = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    Apellido_Paterno = models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100, null=True, blank=True)
    Fecha_Nacimiento = models.DateField(null=True, blank=True)
    Edad = models.IntegerField(null=True, blank=True)
    Sexo = models.CharField(max_length=1, choices=sexo_opciones, null=True, blank=True)
    Estado_Civil = models.CharField(max_length=30, null=True, blank=True)
    Ocupacion = models.CharField(max_length=100, null=True, blank=True)
    Nacionalidad = models.CharField(max_length=30, null=True, blank=True)
    Domicilio = models.CharField(max_length=400, null=True, blank=True)
    Ciudad = models.CharField(max_length=30, null=True, blank=True)
    Telefono = models.CharField(max_length=30, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Foto = models.ImageField(null=True, upload_to='pacientes_fotos', blank=True)
    id_Expediente = models.OneToOneField(Record, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Paciente")
        verbose_name_plural = ("Pacientes")
        ordering = ("-id",)


    def get_fullname(self):
        return str(self.id_Expediente) + ' - ' + self.Nombre + ' ' + self.Apellido_Paterno + ' ' + self.Apellido_Materno

    def __str__(self):
        return self.get_fullname()