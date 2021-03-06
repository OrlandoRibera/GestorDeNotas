# Generated by Django 3.0.5 on 2020-04-26 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materias', '0006_auto_20200425_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='dias',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('LUN', 'Lunes'), ('MAR', 'Martes'), ('MIE', 'Miércoles'), ('JUE', 'Jueves'), ('VIE', 'Viernes'), ('SAB', 'Sábado'), ('DOM', 'Domingo')], max_length=27, verbose_name='Días'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_docente', to=settings.AUTH_USER_MODEL, verbose_name='Docente'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='estudiantes_inscritos',
            field=models.ManyToManyField(blank=True, null=True, related_name='get_inscritos', to=settings.AUTH_USER_MODEL, verbose_name='Inscritos'),
        ),
    ]
