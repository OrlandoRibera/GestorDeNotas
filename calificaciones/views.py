from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, Http404

from materias.models import Materia
from .forms import CalificacionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from calificaciones.models import Calificacion


@method_decorator(login_required, name='dispatch')
class CalificacionAlumnoList(ListView):
    """
        Vista de notas para usuarios con rol Alumno
        El alumno podrá ver la lista de notas que tenga en la materia que está observando
        
        :param id_materia
            Este parámetro lo podemos ver en el archivo urls.py de la app

    """
    model = Calificacion
    # El template es calificacion_list_estudiantes (template para vista de estudiantes
    template_name_suffix = '_list_estudiantes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CalificacionAlumnoList, self).get_context_data(**kwargs)
        # Buscamos si existe una materia con el id pasado por parámetro
        materia = Materia.objects.get(id=self.kwargs['id_materia'])
        if not materia:
            raise Http404
        else:
            # Añadimos al contexto el objeto de la materia
            context['materia'] = materia
        return context

    def get_queryset(self):
        # Calificaciones de ese alumno en la materia pasada por parámetro
        return Calificacion.objects.filter(alumno__calificacion__materia_id=self.kwargs['id_materia']).filter(
            alumno_id=self.request.user.id).distinct()


@method_decorator(login_required, name='dispatch')
class CalificacionDocenteList(ListView):
    """
            Vista de notas para usuarios con rol Docente
            El docente podrá ver la lista de notas que tenga el alumno en la materia

            :param id_materia
            :param id_alumno
                Estos parámetros los podemos ver en el archivo urls.py de la app

        """
    template_name_suffix = '_list_docente'

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario no tiene rol de Docente no puede acceder a la ruta
        if not self.request.user.groups.filter(name='Docente').exists():
            raise Http404
        return super(CalificacionDocenteList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CalificacionDocenteList, self).get_context_data(**kwargs)
        # Buscamos si existe la materia y el alumno con el id pasado por parámetro
        materia = Materia.objects.get(id=self.kwargs['id_materia'])
        alumno = User.objects.get(id=self.kwargs['id_alumno'])

        # Verificamos que el usuario que quiere ingresar a la vista sea el docente de la materia o sea staff de la pág.
        if not materia or not alumno and (
                not materia.docente.id == self.request.user.id or not self.request.user.is_staff):
            raise Http404
        else:
            context['materia'] = materia
            context['alumno'] = alumno
        return context

    def get_queryset(self):
        # Calificaciones de ese alumno (id pasado por parámetro) en la materia dictada por el usuario en sesión
        return Calificacion.objects.filter(alumno_id=self.kwargs['id_alumno']).filter(
            materia__docente_id=self.request.user.id)


@method_decorator(login_required, name='dispatch')
class CalificacionDetailView(DetailView):
    model = Calificacion


@method_decorator(login_required, name='dispatch')
class CalificacionCreate(CreateView):
    """
        Vista de creación de calificación, solo pueden ingresar usuarios con rol Docente
        En la vista no se muestra un input para ingresar la materia ni el alumno, ya que estos
        datos se los envía por URL

        :param id_materia
        :param id_alumno
    """
    model = Calificacion
    form_class = CalificacionForm

    def dispatch(self, request, *args, **kwargs):
        # Verificamos que el usuario tenga rol Docente
        if not self.request.user.groups.filter(name='Docente').exists():
            raise Http404
        return super(CalificacionCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CalificacionCreate, self).get_context_data(**kwargs)
        materia = Materia.objects.get(id=self.kwargs['id_materia'])
        alumno = User.objects.get(id=self.kwargs['id_alumno'])
        context['materia'] = materia
        context['alumno'] = alumno

        # Si el usuario con rol docente no es el docente de la materia retorna 404
        # (Si falla la vista, eliminar la condición, esta se realizó sin realizar pruebas)
        if not self.request.user.id == materia.docente.id:
            raise Http404
        return context

    def form_valid(self, form):
        # Obtenemos el alumno y la materia en la que crearemos la calificación
        form.instance.materia = Materia.objects.get(id=self.kwargs['id_materia'])
        form.instance.alumno = User.objects.get(id=self.kwargs['id_alumno'])
        form.save()
        return super(CalificacionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('calificacion:index_docente',
                            kwargs={'id_materia': self.kwargs['id_materia'], 'id_alumno': self.kwargs['id_alumno']})


@method_decorator(login_required, name='dispatch')
class CalificacionUpdate(UpdateView):
    model = Calificacion
    form_class = CalificacionForm
    template_name_suffix = '_update_form'

    def dispatch(self, request, *args, **kwargs):
        # Verificamos que el usuario tenga rol Docente
        if not self.request.user.groups.filter(name='Docente').exists():
            raise Http404
        return super(CalificacionUpdate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        calificacion = Calificacion.objects.get(id=self.kwargs['pk'])
        return reverse_lazy('calificacion:index_docente',
                            kwargs={'id_materia': calificacion.materia.id, 'id_alumno': calificacion.alumno.id})


@method_decorator(login_required, name='dispatch')
class CalificacionDelete(DeleteView):
    model = Calificacion

    def dispatch(self, request, *args, **kwargs):
        # Verificamos que el usuario tenga rol Docente
        if not self.request.user.groups.filter(name='Docente').exists():
            raise Http404
        return super(CalificacionDelete, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        calificacion = Calificacion.objects.get(id=self.kwargs['pk'])
        return reverse_lazy('calificacion:index_docente',
                            kwargs={'id_materia': calificacion.materia.id, 'id_alumno': calificacion.alumno.id})
