from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from materias.forms import MateriaForm
from materias.models import Materia


@method_decorator(login_required, name='dispatch')
class MateriaListView(ListView):
    """
        Pueden acceder a la vista todos los usuarios registrados en la DB
    """
    model = Materia

    def get_queryset(self):
        # Si el usuario que realizó la petición es staff, puede ver todas las materias que existan, en caso contrario
        # solo podrá ver las materias en la que es Docente o en las que está inscrito como alumno
        if self.request.user.is_staff:
            return Materia.objects.all()
        else:
            return Materia.objects.filter(
                Q(estudiantes_inscritos__id=self.request.user.id) | Q(docente__id=self.request.user.id)).distinct()


@method_decorator(login_required, name='dispatch')
class MateriaDetailView(DetailView):
    model = Materia


@method_decorator((login_required, staff_member_required), name='dispatch')
class MateriaCreate(CreateView):
    """
        Solo puede acceder a la vista un usuario con rol de Staff
    """
    model = Materia
    form_class = MateriaForm
    success_url = reverse_lazy('materia:index')


@method_decorator((login_required, staff_member_required), name='dispatch')
class MateriaUpdate(UpdateView):
    """
        Solo puede acceder a la vista un usuario con rol de staff
    """
    model = Materia
    form_class = MateriaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('materia:index')


@method_decorator((login_required, staff_member_required), name='dispatch')
class MateriaDelete(DeleteView):
    """
        Solo puede acceder a la vista un usuario con rol de staff
    """
    model = Materia
    success_url = reverse_lazy('materia:index')
