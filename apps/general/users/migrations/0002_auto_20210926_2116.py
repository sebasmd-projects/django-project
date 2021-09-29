# Generated by Django 3.1.13 on 2021-09-27 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default='0000', max_length=4, verbose_name='Código de verificación'),
        ),
    ]
