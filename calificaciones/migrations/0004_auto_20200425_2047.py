# Generated by Django 3.0.5 on 2020-04-26 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0006_auto_20200425_2047'),
        ('calificaciones', '0003_auto_20200425_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materias.Materia'),
        ),
    ]