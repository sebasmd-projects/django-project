from django.db import models
from django.utils. translation import gettext as _


class RedesSocialesModel(models.Model):
    name = models.CharField(_('Red Social'), max_length=50)
    key = models.SlugField(_('Referencia'), max_length=10, unique=True)
    url = models.URLField(_('Enlace'), max_length=400, null=True, blank=True)
    created = models.DateTimeField(_('Fecha de cración'), auto_now_add=True)
    updated = models.DateTimeField(_('Fecha de edición'), auto_now=True)

    class Meta:
        verbose_name = _('Red Social')
        verbose_name_plural = _('Redes Sociales')
        unique_together = ('name', 'key')
        ordering = ['id']

    def __str__(self):
        string = "{} {} {}".format(self.id, self.name, self.key)
        return string


class TypingIndexModel(models.Model):
    typing_key = models.SlugField(_('Referencia'), max_length=20, unique=True)
    typing_name = models.CharField(_('Palabras'), max_length=200)
    created = models.DateTimeField(_('Fecha de cración'), auto_now_add=True)
    updated = models.DateTimeField(_('Fecha de edición'), auto_now=True)

    class Meta:
        verbose_name = _('Palabras del inicio (Typing)')
        verbose_name_plural = _('Palabras del inicio (Typing)')
        ordering = ['id']

    def __str__(self):
        string = "{} {}".format(self.id, self.typing_name)
        return string


class TitleModel(models.Model):
    title_key = models.SlugField(_('Referencia'), max_length=20, unique=True)
    title = models.CharField(_('Título'), max_length=100)
    created = models.DateTimeField(_('Fecha de cración'), auto_now_add=True)
    updated = models.DateTimeField(_('Fecha de edición'), auto_now=True)

    class Meta:
        verbose_name = _('Título del Inicio')
        verbose_name_plural = _('Título del Inicio')
        ordering = ['id']

    def __str__(self):
        string = "{} {}".format(self.id, self.title)
        return string


class AppNameModel(models.Model):
    app_key = models.SlugField(_('Referencia'), max_length=20, unique=True)
    title = models.CharField(_('Título'), max_length=100)
    created = models.DateTimeField(_('Fecha de cración'), auto_now_add=True)
    updated = models.DateTimeField(_('Fecha de edición'), auto_now=True)

    class Meta:
        verbose_name = _('Nombre de la App o Empresa')
        verbose_name_plural = _('Nombre de la App o Empresa')
        ordering = ['id']

    def __str__(self):
        string = "{} {}".format(self.id, self.title)
        return string
