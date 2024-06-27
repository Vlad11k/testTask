# Generated by Django 5.0.6 on 2024-06-27 02:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('date_end', models.DateTimeField(blank=True, verbose_name='Дата закрытия')),
                ('report', models.TextField(default='', verbose_name='Отчёт')),
                ('status', models.CharField(choices=[('WAITING', 'Ожидает исполнителя'), ('PROCESS', 'В процессе'), ('COMPLETED', 'Выполнена')], default='WAITING')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client', to='clients.client', verbose_name='Заказчик')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee', to='employees.employee', verbose_name='Сотрудник')),
            ],
        ),
    ]
