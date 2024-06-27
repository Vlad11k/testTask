from django.db import models

from employees.models import Employee
from clients.models import Client


class Task(models.Model):
    WAITING = 'WAITING'
    PROCESS = 'PROCESS'
    COMPLETED = 'COMPLETED'
    STATUS_CHOICES = {
        WAITING: 'Ожидает исполнителя',
        PROCESS: 'В процессе',
        COMPLETED: 'Выполнена',
    }

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='client',
        verbose_name='Заказчик'
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        null=True,
        related_name='employee',
        verbose_name='Сотрудник'
    )
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    date_end = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')
    report = models.TextField(default=None, verbose_name='Отчёт')
    status = models.CharField(
        choices=STATUS_CHOICES,
        default=WAITING,
    )
