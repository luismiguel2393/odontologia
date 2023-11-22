from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here

class Usuarios(AbstractBaseUser):
    username= models.AutoField('Nombre de usuario',unique =True, max_length=100)
    email = models.EmailField('Correo Electronico',max_langth=254, unique=True)
    nombre1 = models.CharField('Nombre', max_length=50)
    nombre2 = models.CharField('Nombre', max_length=50)
    apellido1 = models.CharField('Apellido', max_length=50)
    apellido2 = models.CharField('Apellido', max_length=50)  
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=True)