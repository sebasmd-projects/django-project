from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'username',
        'email',
        'phone',
        'newsletter',
        'id',
        'is_staff',
        'is_superuser',
        'is_active'
    )

    readonly_fields = ('created', 'updated')