from django.db import models

# Create your models here.

# Create your models here.

ram_options = [('2', '2gb'),
               ('2exp', '2gb(exp)'),
               ('4', '4gb'),
               ('4exp', '4gb(exp)'),
               ('8', '8gb'),
               ('8exp', '8gb(exp)'),
               ('16', '16gb'),
               ('16exp', '16gb(exp)'),
               ('32', '32gb'),
               ('32xp', '32gb(exp)')]

screen = [('13pulg', '13 pulgadas'),
          ('14pulg', '14 pulgadas'),
          ('15.6pulg', '15.6 pulgadas'),
          ('17pulg', '17 pulgadas')]

ssdm2 = [('256gb', '256 gb'),
          ('512gb', '512 gb'),
          ('1tb', '1 tb'),
          ('2tb', '2 tb')]

hardisk = [('sinhdd', 'sin HDD'),
           ('256hdd', '256 gb'),
           ('512hdd', '512 gb'),
           ('1hdd', '1 tb'),
           ('2hdd', '2 tb')]
class Registrar_Laptop(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20,unique=True)
    nombre = models.CharField(max_length=20) 
    stock = models.IntegerField()
    precio = models.IntegerField()
    pantalla = models.CharField(max_length=10, choices = screen)
    teclado = models.CharField(max_length=10)
    procesador = models.CharField(max_length=25)
    ram = models.CharField(max_length=10, choices = ram_options)
    color = models.CharField(max_length=15)
    m2 = models.CharField(max_length=10, choices = ssdm2)
    hdd = models.CharField(max_length=10, choices = hardisk)
    grafica = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=1000)
    imagen_1 = models.ImageField(upload_to="proyecto/static/imagenes", null=True)
    imagen_2 = models.ImageField(upload_to="proyecto/static/imagenes", null=True)
    imagen_3  = models.ImageField(upload_to="proyecto/static/imagenes", null=True)
    imagen_4 = models.ImageField(upload_to="proyecto/static/imagenes", null=True)


class vender_Laptop(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20,unique=True)     
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    fecha = models.DateField()
    cliente = models.CharField(max_length=35)
    direccion = models.CharField(max_length=25)
    ci = models.IntegerField()
    telefono = models.IntegerField()