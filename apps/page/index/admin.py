from django.contrib import admin
from . import models


@admin.register(models.AppNameModel)
class AppNameModelAdmin(admin.ModelAdmin):
    list_display = (
        'app_key',
        'title',
    )
    
    readonly_fields = (
        'created',
        'updated'
    )

@admin.register(models.RedesSocialesModel)
class RedesSocialesModelAdmin(admin.ModelAdmin):
    list_display = (
        'key',
        'name'
    )

    search_fields = (
        'key',
        'name',
    )

    list_filter = (
        'name',
    )

    readonly_fields = (
        'created',
        'updated'
    )


@admin.register(models.TypingIndexModel)
class TypingIndexModelAdmin(admin.ModelAdmin):
    list_display = (
        'typing_key',
        'typing_name',
    )

    readonly_fields = (
        'created',
        'updated'
    )


@admin.register(models.TitleModel)
class TitleModelAdmin(admin.ModelAdmin):
    list_display = (
        'title_key',
        'title',
    )

    readonly_fields = (
        'created',
        'updated'
    )

