from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')

    fieldsets = [
        (None, {"fields": ["email"]}),
        ("Личная информация", {"fields": ["full_name", "phone"]}),
        ("Права", {"fields": ["is_staff"]}),
    ]
