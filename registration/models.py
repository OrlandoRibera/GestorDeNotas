from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Usuario(User):
    """
        Modelo no utilizado a nivel de base de datos, los únicos datos utilizados de esta clase es la variable
        TIPO_USUARIOS
    """
    Docente = 'Docente'
    Alumno = 'Alumno'

    TIPO_USUARIOS = (
        (Docente, 'Docente'),
        (Alumno, 'Alumno'),
    )

    tipo = models.CharField(choices=TIPO_USUARIOS, default=Alumno, max_length=20)
