from django.contrib.auth.models import User
from django.db import models

from materias.models import Materia


class Calificacion(models.Model):
    TIPO_CALIFICACION = (
        ('Primer parcial', '1er Parcial'),
        ('Segundo parcial', '2do Parcial'),
        ('Exámen final', 'Ex. Final'),
        ('Control', 'Control'),
        ('Prácticos', 'Prácticos'),
    )
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, blank=True)
    nota = models.DecimalField(max_digits=4, decimal_places=1)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(choices=TIPO_CALIFICACION, default='Primer Parcial', max_length=100)

    def __str__(self):
        return self.alumno.last_name + ' ' + self.alumno.first_name + ' - ' + self.materia.nombre + ': ' + self.tipo
