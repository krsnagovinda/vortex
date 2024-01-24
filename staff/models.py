from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Staff(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    Nombre = models.CharField(max_length=50)
    Apellido_Paterno = models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100)    
    Telefono = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    Foto = models.ImageField(default='default.jpg', blank=True, null=True, upload_to='staff/')


    def get_fullname(self):
        return self.Nombre + '  ' + self.Apellido_Paterno + '  ' + self.Apellido_Materno

    class Meta:
        verbose_name = ("staff")
        verbose_name_plural = ("staff")
        ordering = ("-id",)

    def __str__(self):
        return self.get_fullname()