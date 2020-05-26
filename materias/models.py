from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.


class Materia(models.Model):
    DAYS = (
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    )
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    docente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                blank=True, verbose_name='Docente', related_name='get_docente')
    # docente = models.ForeignKey(User.objects.filter(groups__name='Docente'), on_delete=models.SET_NULL, null=True,
    #                             blank=True, verbose_name='Docente', related_name='docente')
    dias = MultiSelectField(choices=DAYS, verbose_name='Días')
    hora_inicio = models.TimeField(verbose_name='Hora de inicio')
    hora_fin = models.TimeField(verbose_name='Hora de fin')
    estudiantes_inscritos = models.ManyToManyField(User, verbose_name='Inscritos',
                                                   related_name='get_inscritos', null=True, blank=True)
    creditos = models.PositiveSmallIntegerField(default=4)
    semestre = models.PositiveSmallIntegerField(default=1)
    estado = models.BooleanField(verbose_name='¿Habilitada?', default=False)

    def __str__(self):
        return str(
            self.nombre + ': ' + self.docente.last_name + ' ' + self.docente.first_name + ' de ' + self.hora_inicio.__str__() + ' a ' + self.hora_fin.__str__())
