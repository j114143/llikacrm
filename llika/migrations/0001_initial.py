# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_inicio', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Cargo de Personal',
            },
        ),
        migrations.CreateModel(
            name='ControlAsistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora_llegada', models.TimeField()),
                ('hora_salida', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Control Asistencia',
            },
        ),
        migrations.CreateModel(
            name='InformacionPracticas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='TareasEncargadas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('proyecto', models.ForeignKey(to='llika.Proyecto')),
            ],
            options={
                'verbose_name_plural': 'Tareas Encargadas',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('DNI', models.CharField(max_length=8)),
                ('fecha_nacimiento', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30, blank=True)),
                ('celular', models.CharField(max_length=30, blank=True)),
                ('e_mail_personal', models.CharField(max_length=30, blank=True)),
                ('e_mail_llika', models.CharField(max_length=30)),
                ('contacto', models.CharField(max_length=30)),
                ('contacto_telefono', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Personal de Llika',
            },
        ),
        migrations.AddField(
            model_name='tareasencargadas',
            name='trabajadores',
            field=models.ForeignKey(to='llika.Trabajador'),
        ),
        migrations.AddField(
            model_name='informacionpracticas',
            name='institucion',
            field=models.ForeignKey(to='llika.Institucion'),
        ),
        migrations.AddField(
            model_name='informacionpracticas',
            name='practicante',
            field=models.OneToOneField(to='llika.Trabajador'),
        ),
        migrations.AddField(
            model_name='controlasistencia',
            name='trabajador',
            field=models.OneToOneField(to='llika.Trabajador'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='Trabajador',
            field=models.ForeignKey(to='llika.Trabajador'),
        ),
    ]
