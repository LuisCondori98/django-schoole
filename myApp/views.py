from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from myApp.models import Curso
from myApp.forms import CursoFormulario

# Create your views here.

# def cursos(self):
  
#   cursos = Curso.objects.all()
  
#   plantilla = loader.get_template("index.html")
  
#   context = {"cursos":cursos}
  
#   document = plantilla.render(context)
    
#   return HttpResponse(document)

def inicio(request):
  
  #return HttpResponse("vista inicio")
  return render(request, "myApp/index.html")

def cursos(request):
  
  cursos = Curso.objects.all()
  
  plantilla = loader.get_template("myApp/cursos.html")
  
  context = {"cursos": cursos}
  
  document = plantilla.render(context)
  
  # return HttpResponse(document)
  
  #return HttpResponse("vista cursos")
  return render(request, "myApp/cursos.html", {"cursos": cursos})

def cursosForm(request):
  
  # if request.method == "POST":
    
  #   miFormulario = CursoFormulario(request.POST)
    
  #   print(miForm)
    
  #   if miFormulario.is_valid:
      
  #     info = miFormulario.cleaned_data
      
  #     curso = Curso(nombre = info['nombre'], camada = info['camada'])
      
  #     curso.save()
      
  #     return render(request, "myApp/index.html", {"miForm": miFormulario})
    
  # else:
    
  #   miForm = CursoFormulario()
  
  if request.method == 'POST':
    
    n_curso = request.POST["curso"]
    
    n_camada = request.POST["camada"]
    
    curso = Curso(nombre = n_curso, camada = n_camada)
    
    print(n_curso, n_camada)
    
    curso.save()
  
  return render(request, "myApp/cursosForm.html")

def profesores(request):
  
  if request.method == 'POST':
    
    nombre = request.POST['nombre']
    
    print(nombre)
  
  #return HttpResponse("vista profesores")
  return render(request, "myApp/profesores.html")

def estudiantes(request):
  
  #return HttpResponse("vista estudiantes")
  return render(request, "myApp/estudiantes.html")

def entregables(request):
  
  #return HttpResponse("vista entregables")
  return render(request, "myApp/entregables.html")