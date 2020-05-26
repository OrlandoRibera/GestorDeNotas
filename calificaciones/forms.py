from django import forms

from calificaciones.models import Calificacion


class CalificacionForm(forms.ModelForm):
    materia = forms.TextInput(attrs={'class': 'form-control', })
    alumno = forms.TextInput(attrs={'class': 'form-control', })
    nota = forms.DecimalField(decimal_places=1, max_digits=4, initial=00.0, max_value=100, min_value=0,
                              widget=forms.NumberInput(attrs={
                                  'class': 'form-control',
                              }))
    tipo = forms.ChoiceField(choices=Calificacion.TIPO_CALIFICACION, widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Calificacion
        fields = ['nota', 'tipo', ]
        labels = {
            'materia': 'Materia',
            'alumno': 'Alumno'
        }
