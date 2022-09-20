
from django.shortcuts import render, redirect
from .models import Agenda

# Create your views here.
def home(request):
    agendas= Agenda.objects.all()
    return render(request, "gestionAgenda.html",{"agendas": agendas})

def registrarContacto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    telefono=request.POST['numtelefono']
    email=request.POST['txtemail']

    agenda = Agenda.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, telefono=telefono, email=email)
    return redirect('/')

def edicionAgenda(request, codigo):
    agenda = Agenda.objects.get(codigo=codigo)
    return render(request, "edicionAgenda.html", {"agenda": agenda})

def editarAgenda(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    telefono=request.POST['numtelefono']
    email=request.POST['txtemail']

    agenda = Agenda.objects.get(codigo=codigo)
    agenda.nombre = nombre
    agenda.apellido = apellido
    agenda.telefono = telefono
    agenda.email = email
    agenda.save()

    

    return redirect('/')

def eliminarAgenda(request, codigo):
    agenda= Agenda.objects.get(codigo=codigo)
    agenda.delete()

    return redirect('/')
