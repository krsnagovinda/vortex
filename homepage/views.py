from django.shortcuts import render, redirect, get_object_or_404
from paciente.models import Paciente


# Create your views here.
def home(request):  
    cuantos = Paciente.objects.all().count()  
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

