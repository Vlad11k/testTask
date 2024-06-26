from django.db import models


class Employee(models.Model):

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
        blank=True
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True,
        verbose_name="Фото"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
