from django.db import models
from ckeditor.fields import RichTextField
from django.utils. translation import gettext as _
from . import managers
from apps.general.users.models import PersonModel


class ManyToManyGeneral(models.Model):
    name = models.CharField(_('Nombre'), max_length=100)
    created = models.DateTimeField(_('Fecha de cración'), auto_now_add=True)
    updated = models.DateTimeField(_('Fecha de edición'), auto_now=True)

    class Meta:
        verbose_name = _('m2m General')
        verbose_name_plural = _('m2m General')
        ordering = ['id']
        abstract = True


class CountersModel(ManyToManyGeneral):
    counter_amount = models.CharField(_('Cantidad del Contador'), max_length=8)
    counter_icon = models.CharField(_('Icono'), max_length=50)

    class Meta:
        verbose_name = _('Contador')
        verbose_name_plural = _('Contadores')
        ordering = ['id']

    def __str__(self):
        string = "{} {} {}".format(
            self.id, self.name, self.counter_amount)
        return string


class SkillsModel(ManyToManyGeneral):
    skills_percentage = models.IntegerField(_('Porcentage de la habilidad'))

    class Meta:
        verbose_name = _('Habilida')
        verbose_name_plural = _('Habilidades')
        ordering = ['id']

    def __str__(self):
        string = "{} {}".format(self.id, self.name)
        return string


class InterestsModel(ManyToManyGeneral):
    interest_icon = models.CharField(_('Icono'), max_length=50)
    interest_icon_color = models.CharField(_('Color del Icono'), max_length=50)

    class Meta:
        verbose_name = _('Interes')
        verbose_name_plural = _('Intereses')
        ordering = ['id']

    def __str__(self):
        string = "{} {}".format(self.id, self.name)
        return string


class TestimonialModel(ManyToManyGeneral):
    testimonial_work = models.CharField(
        _('Ocupación o Profesión'), max_length=50)
    testimonial_text = RichTextField(_('Testimonio'))

    class Meta:
        verbose_name = _('Testimonio')
        verbose_name_plural = _('Testimonios')
        ordering = ['id']

    def __str__(self):
        string = "{} {} {}".format(
            self.id, self.name, self.testimonial_work)
        return string


class AboutModel(PersonModel):
    description_1 = RichTextField(_('Descripción 1'))
    description_2 = RichTextField(_('Descripción 2'))
    web_page = models.CharField(
        _('Página Web'), max_length=50, blank=True, null=True)
    grade = models.CharField(_('Grado de educación'), max_length=30)
    freelance = models.CharField(
        _('Disponibilidad como Freelance'), max_length=30)
    strength_1 = RichTextField(_('Fortaleza 1'), blank=True, null=True)
    strength_2 = RichTextField(_('Fortaleza 2'), blank=True, null=True)
    counters = models.ManyToManyField(CountersModel)
    skills = models.ManyToManyField(SkillsModel)
    interests = models.ManyToManyField(InterestsModel)
    testimonials = models.ManyToManyField(TestimonialModel, blank=True)

    objects = managers.AboutModelManager()

    class Meta:
        verbose_name = _('Información Conóceme')
        verbose_name_plural = _('Información Conóceme')
        ordering = ['id']
        unique_together = ('phone', 'email')

    def __str__(self):
        string = "{} {} {}".format(self.id, self.names, self.surname)
        return string
