from django.contrib import admin
from django.urls import path, include

from calificaciones.urls import calificaciones_patterns
from core.views import index as core_index
from materias.urls import materia_patterns

urlpatterns = [
    path('', core_index, name='index'),
    path('materias/', include(materia_patterns), name='materia'),
    path('calificaciones/', include(calificaciones_patterns), name='calificacion'),

    path('admin/', admin.site.urls),

    # Path de auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

]
