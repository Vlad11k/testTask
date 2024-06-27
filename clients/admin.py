from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')

    fieldsets = [
        (None, {"fields": ["email"]}),
        ("Личная информация", {"fields": ["full_name", "phone"]}),
    ]

