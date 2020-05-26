from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from registration.models import Usuario


class UserCreation(UserCreationForm):
    tipo = forms.ChoiceField(choices=Usuario.TIPO_USUARIOS, widget=forms.Select(attrs={
        'class': 'form-control mb-2'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'tipo')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'username': 'Nombre de usuario',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya está registrado, prueba con otro')
        return email
