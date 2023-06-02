from django.urls import path
from . import views
from Aplicaciones.Academico.views import *

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('FormularioCurso/', FormularioCurso, name="FormularioCurso"),
    path('busquedaCurso/', busquedaCurso, name="busquedaCurso"),
    path('busqueda', buscar, name="Buscar"),
]