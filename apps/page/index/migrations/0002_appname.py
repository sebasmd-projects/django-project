# Generated by Django 3.1.13 on 2021-09-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_key', models.SlugField(max_length=20, unique=True, verbose_name='Referencia')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Nombre de la App o Empresa',
                'verbose_name_plural': 'Nombre de la App o Empresa',
                'ordering': ['id'],
            },
        ),
    ]
