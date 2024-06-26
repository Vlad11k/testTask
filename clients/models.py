from django.db import models


class Client(models.Model):
    full_name = models.CharField(
        verbose_name='ФИО',
        max_length=150,
        blank=True)
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
        blank=True
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=100,
        unique=True,
        blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


