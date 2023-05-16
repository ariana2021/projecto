from django.db import models

# Create your models here.
           
class Muralista(models.Model):
    id_muralista = models.CharField(primary_key=True, max_length=100)
    nombre = models.CharField(max_length=50) 
    apellidos = models.CharField(max_length=50)
    seudonimo = models.CharField(max_length=50)
    foto = models.BinaryField(max_length=10, default=b'\x08')
    murales  = models.CharField(max_length=200)
    celular = models.IntegerField()
    instagram = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    correo = models.EmailField()
    
    
class Mural(models.Model):
     idMural = models.CharField(primary_key=True, max_length=100)
     nombre_mural = models.CharField(max_length=50)
     direccion = models.CharField(max_length=100)
     date = models.DateField()
     imagen = models.BinaryField(max_length=10, default=b'\x08')
     descripcion = models.CharField(max_length=100)
     id_muralista = models.ForeignKey(Muralista, on_delete=models.CASCADE) 

    
class Colores(models.Model):
    idColores = models.CharField(primary_key=True, max_length=6)
    nombre_color = models.CharField(max_length=200) 
    codigo = models.CharField(max_length=20)
    red= models.CharField(max_length=200) 
    green = models.CharField(max_length=200) 
    blue = models.CharField(max_length=200) 
    
class Paleta(models.Model):
    idMural = models.ForeignKey(Mural, on_delete=models.CASCADE) 
    idColores = models.ForeignKey(Colores, on_delete=models.CASCADE) 


