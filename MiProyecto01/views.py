from django.http import HttpResponse
import datetime
from django.template import loader

def saludo(request):
  
  return HttpResponse("Hola mundo Django")

def nombre(self, nombre):
  
  documentoTexto = f"<div><h1>Mi nombre es : {nombre}</h1></div>"
  
  return HttpResponse(documentoTexto)

def nacimiento(self, anio):
  
  anioNacimiento = datetime.date.today().year - int(anio)
  
  documentoTexto = f"<div>Año que naciste : {anioNacimiento}<h1>"
  
  return HttpResponse(documentoTexto)

def probandoTemplate(self, nombre, apellido):
  
  #nom = "Luis"
  #ap = "Condori"
  
  alumnos = ["Juan", "Luis", "Fiorella", "Maria", "Jhoselyn"]
  
  diccionario = {"curso": "Java", "nombre": nombre, "apellido": apellido, "hoy": datetime.datetime.now(), "alumnos": alumnos}
  
  #miHtml = open("./../plantillas/template.html")
  
  #print(miHtml)
  
  plantilla = loader.get_template("template.html")
  
  document = plantilla.render(diccionario)
  
  return HttpResponse(document)

# def curso(self):
  
#   curso = Curso(nombre = "PHP", camada = 789)
  
#   curso.save()
  
#   documentoTexto = f"Curso: {curso.nombre}  camada: {curso.camada}"
  
#  return HttpResponse(documentoTexto)