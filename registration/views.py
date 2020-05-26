from django import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import azy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from registration.forms import UserCreation


@method_decorator(staff_member_required, name='dispatch')
class SignUpView(CreateView):
    form_class = UserCreation
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        tipo = form.cleaned_data['tipo']

        # Creamos el usuario para luego asignarle el rol
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Asignación de Rol
        if tipo == 'Docente':
            # id 1 es el rol de Docente
            user.groups.add(Group.objects.get(id=1))
        else:
            #  id 2 es el rol de Alumno
            user.groups.add(Group.objects.get(id=2))

        return redirect('index')

    def get_success_url(self):
        return azy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar widgets en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Nombre de usuario'
        })
        form.fields['first_name'].widget = forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Nombres'
        })
        form.fields['last_name'].widget = forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Apellidos'
        })
        form.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Dirección Email'
        })
        form.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Contraseña'
        })
        form.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Repite la Contraseña'
        })
        return form
