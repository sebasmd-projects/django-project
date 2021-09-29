from django.contrib import admin
from . import models


@admin.register(models.CountersModel)
class CountersModelAdmin(admin.ModelAdmin):
    list_display = ('id','name')

    readonly_fields = ('created', 'updated')


@admin.register(models.SkillsModel)
class SkillsModelAdmin(admin.ModelAdmin):
    list_display = ('id','name')

    readonly_fields = ('created', 'updated')


@admin.register(models.InterestsModel)
class InterestsModelAdmin(admin.ModelAdmin):
    list_display = ('id','name')

    readonly_fields = ('created', 'updated')


@admin.register(models.TestimonialModel)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ('id','name')

    readonly_fields = ('created', 'updated')


@admin.register(models.AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'age',
        'phone',
        'email',
    )

    """
    search_fields = (
        'id',
        'names',
        'surname',
    )

    list_filter = ('phone','email')
    """

    filter_horizontal = ('skills','interests','testimonials','counters')

    readonly_fields = ('created', 'updated')