# Generated by Django 3.1.13 on 2021-09-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TitleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_key', models.SlugField(max_length=20, unique=True, verbose_name='Referencia')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Título del Inicio',
                'verbose_name_plural': 'Título del Inicio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypingIndexModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typing_key', models.SlugField(max_length=20, unique=True, verbose_name='Referencia')),
                ('typing_name', models.CharField(max_length=200, verbose_name='Palabras')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Palabras del inicio (Typing)',
                'verbose_name_plural': 'Palabras del inicio (Typing)',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RedesSocialesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Red Social')),
                ('key', models.SlugField(max_length=10, unique=True, verbose_name='Referencia')),
                ('url', models.URLField(blank=True, max_length=400, null=True, verbose_name='Enlace')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
                'ordering': ['id'],
                'unique_together': {('name', 'key')},
            },
        ),
    ]