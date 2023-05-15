from django.db import models

# Create your models here.
       
class Contacto(models.Model):
    celular = models.CharField(max_length=9) 
    instagram = models.CharField(max_length=100)
    facebook= models.CharField(max_length=200)     
    def _str_(self):
         return self.celular
   
class Estilo(models.Model):
    nombre_color = models.CharField(max_length=200)  
    
     
class Muralista(models.Model):
    nombre = models.CharField(max_length=200) 
    apellidos = models.CharField(max_length=200)
    seudonimo = models.CharField(max_length=200)
    foto = models.BinaryField(max_length=10, default=b'\x08')
    contacto = models.ForeignKey(Contacto , on_delete=models.CASCADE) #oneToOne (pk)
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    
    def _str_(self):
         return self.nombre
    
class Color(models.Model):
    
    idColor = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=200) 
    rgb = models.CharField(max_length=200) 
    red= models.CharField(max_length=200) 
    green = models.CharField(max_length=200) 
    blue = models.CharField(max_length=200) 
    
    def _str_(self):
            return self.nombre
  
class Paleta(models.Model):
    idPaleta = models.CharField(primary_key=True, max_length=6)
    color = models.ForeignKey(Color, on_delete=models.CASCADE) 
    muralista = models.ForeignKey(Muralista , on_delete=models.CASCADE)      