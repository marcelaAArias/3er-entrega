from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def FormularioCurso(request):

    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        nombre = Curso(nombre=request.POST['nombre'], codigo=request.POST['codigo'])

        Curso.save()

        return render(request, "gestionCurso.html")
    return render(request, "FormularioCurso.html")    
        
        
def busquedaCurso(request):
    return render(request, "busquedaCurso.html")

def buscar(request):

    if  request.GET["nombre"]:
        nombre = request.GET["nombre"]
        nombre = Curso.objects.filter(nombre__icontains=nombre)

        return render(request, "resultadosBusquedas.html", {"codigo": Curso, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)    

   
def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Curso registrado!')
    return redirect('/')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/')