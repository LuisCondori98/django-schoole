from django.urls import path
from myApp import views

urlpatterns = [
    #path('saludo/', views.saludo),
    #path('nombre/<nombre>/', nombre),
    #path('nacimiento/<anio>/', nacimiento),
    #path('template/<nombre>/<apellido>/', probandoTemplate),
    #path('curso/', curso),
    #path('cursos/', cursos)
    path("", views.inicio, name="Inicio"),
    path("cursos/", views.cursos, name="Cursos"),
    path("profesores/", views.profesores, name="Profesores"),
    path("estudiantes/", views.estudiantes, name="Estudiantes"),
    path("entregables/", views.entregables, name="Entregables"),
    path("cursos/crear/", views.cursosForm, name="cursosForm"),
]