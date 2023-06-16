from django.contrib.auth.forms import UsernameField
from django.db import models

# Create your models here.



class Proveedor(models.Model):
    id_proveedor =models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    def __str__(self):
        return self.nombres   

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    def __str__(self):
        return self.nombres


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    

    def __str__(self):
        return self.nombre

opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    id_producto = models.IntegerField()
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()