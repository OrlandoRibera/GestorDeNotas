from django.contrib.auth.decorators import permission_required
from django.urls import path

from . import views
from .views import CalificacionDetailView, CalificacionCreate, CalificacionUpdate, \
    CalificacionDelete, CalificacionAlumnoList, CalificacionDocenteList

calificaciones_patterns = ([
                               # Id de materia, le cargará la lista de notas en esa materia
                               path('<int:id_materia>/', CalificacionAlumnoList.as_view(), name='index_alumno'),

                               path('<int:id_materia>/<int:id_alumno>/', CalificacionDocenteList.as_view(),
                                    name='index_docente'),
                               path('create/<int:id_materia>/<int:id_alumno>/', CalificacionCreate.as_view(),
                                    name='create'),
                               path('update/<int:pk>/', CalificacionUpdate.as_view(), name='update'),
                               path('delete/<int:pk>/', CalificacionDelete.as_view(), name='delete'),

                           ], 'calificacion')
