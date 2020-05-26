from django import forms
from django.contrib.auth.models import User

from materias.models import Materia


class MateriaForm(forms.ModelForm):
    nombre = forms.TextInput(attrs={'class': 'form-control', })
    docente = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Docente'),
                                     widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    # docente = forms.ChoiceField(
    #     choices=[(docente.pk, docente) for docente in User.objects.filter(groups__name='Docente')],
    #     widget=forms.Select(attrs={'class': 'form-control', }))
    dias = forms.MultipleChoiceField(choices=Materia.DAYS, widget=forms.CheckboxSelectMultiple)
    hora_inicio = forms.TimeField(
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}, format='%H:%M'), label='Hora de inicio')
    hora_fin = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}, format='%H:%M'),
                               label='Hora de finalización')
    estudiantes_inscritos = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(groups__name='Alumno'), required=False)
    creditos = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control-sm'}), min_value=1,
                                  max_value=4,
                                  error_messages={'invalid': 'Valores entre 1 y 4', })
    semestre = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control-sm'}), min_value=1,
                                  max_value=10, error_messages={'invalid': 'Valores entre 1 y 4'})
    estado = forms.BooleanField(required=False, label='¿Habilitada?')

    class Meta:
        model = Materia
        fields = ['nombre', 'docente', 'dias', 'hora_inicio', 'hora_fin', 'estudiantes_inscritos', 'creditos',
                  'semestre', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la materia'
            }),
        }

    labels = {
        'nombre': 'Nombre',
        'docente': 'Docente'
    }
