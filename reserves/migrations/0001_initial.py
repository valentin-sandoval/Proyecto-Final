# Generated by Django 5.0.3 on 2024-04-17 01:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Suplente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField(default=datetime.datetime.now)),
                ('fecha_fin', models.DateField(default=datetime.datetime.now)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarjetas', to='reserves.estado')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarjetas', to='reserves.profesor')),
                ('suplente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarjetas', to='reserves.suplente')),
            ],
        ),
    ]