from django.contrib import admin

# Register your models here.
from calificaciones.models import Calificacion
from materias.models import Materia

admin.site.register(Calificacion)
admin.site.register(Materia)
