
from django.db import models

# Create your models here.
class Agenda(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.PositiveIntegerField()
    email=models.CharField(max_length=100)
    
    def __str__(self):
        texto ="{0} ({1})"
        return texto.format(self.nombre, self.apellido, self.telefono, self.email)