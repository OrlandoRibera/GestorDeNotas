from django.contrib.auth.decorators import permission_required
from django.urls import path

from materias.views import MateriaListView, MateriaDetailView, MateriaCreate, MateriaUpdate, MateriaDelete

materia_patterns = ([
                        path('', MateriaListView.as_view(), name='index'),
                        path('<int:pk>/', MateriaDetailView.as_view(), name='materia'),
                        path('create/', permission_required('is_staff')(MateriaCreate.as_view()), name='create'),
                        path('update/<int:pk>/', permission_required('is_staff')(MateriaUpdate.as_view()),
                             name='update'),
                        path('delete/<int:pk>/', permission_required('is_staff')(MateriaDelete.as_view()),
                             name='delete'),
                    ], 'materia')
