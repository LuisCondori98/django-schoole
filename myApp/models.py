from django.db import models

# Create your models here.
class Curso(models.Model):
  
  nombre = models.CharField(max_length=40)
  camada = models.IntegerField()
  
  def __str__(self):
    
    return f"Curso: {self.nombre} - Camada: {self.camada}"
  
class Estudiante(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  mail = models.EmailField()
  
  def __str__(self):
    
    return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.mail}"
  
class Profesor(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  mail = models.EmailField()
  profesion = models.CharField(max_length = 30)
  
class Entregable(models.Model):
  nombre = models.CharField(max_length=30)
  fechaEntrega = models.DateField()
  entregado = models.BooleanField()