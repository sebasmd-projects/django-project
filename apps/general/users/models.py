from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils. translation import gettext as _
from .managers import UserManager
from .signals import optimize_image, user_directory_path
from django.db.models.signals import post_save


class PersonModel(models.Model):
    avatar = models.ImageField(
        _('Foto de perfil'), upload_to=user_directory_path, blank=True, null=True)
    email = models.EmailField(_('Correo'), unique=True)
    phone = models.CharField(_('Celular'), max_length=20, unique=True)
    names = models.CharField(
        _('Nombres'), max_length=50)
    surname = models.CharField(
        _('Apellidos'), max_length=50)
    country = models.CharField(_('País'), max_length=50, blank=True, null=True)
    city = models.CharField(_('Ciudad'), max_length=100, blank=True, null=True)
    full_name = models.CharField(
        _('Nombres y Apellidos'), max_length=100, editable=False, blank=True, null=True)
    birthday = models.DateField(
        _('Fecha de nacimiento'), auto_now=False, auto_now_add=False)
    age = models.CharField(_('Edad'), max_length=4,
                           editable=False)
    gender = models.CharField(_('Sexo'), max_length=50, blank=True, null=True)
    privacy = models.BooleanField(_('Términos y condiciones'), default=False)
    newsletter = models.BooleanField(
        _('Recibir más información'), default=False)
    created = models.DateTimeField(_('Fecha de cración'), auto_now_add=True)
    updated = models.DateTimeField(_('Fecha de edición'), auto_now=True)

    class Meta:
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')
        ordering = ['id']
        unique_together = ('username', 'email', 'phone')
        abstract = True

    def save(self, *args, **kwargs):
        self.full_name = "{} {}".format(self.names, self.surname)
        self.age = date.today().year - self.birthday.year - ((date.today().month,
                                                              date.today().day) < (self.birthday.month, self.birthday.day))
        super(PersonModel, self).save(*args, **kwargs)

    def __str__(self):
        string = "{} {} {}".format(self.id, self.full_name)
        return string


post_save.connect(optimize_image, sender=PersonModel)


class User(PersonModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Usuario'), max_length=16, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    verification_code = models.CharField(
        _('Código de verificación'), max_length=4, default='0000')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'phone',
        'names',
        'surname',
        'birthday',
        'privacy',
        'is_active'
    ]

    objects = UserManager()

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        ordering = ['id']
        unique_together = ('username', 'email')

    def __str__(self):
        string = "{} {}".format(self.full_name, self.username)
        return string
