from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'get_email', 'get_phone')

    @admin.display(description='ФИО')
    def get_full_name(self, obj):
        return f"{obj.user.full_name}"

    @admin.display(description='Email')
    def get_email(self, obj):
        return f"{obj.user.email}"

    @admin.display(description='Телефон')
    def get_phone(self, obj):
        return f"{obj.user.phone}"

