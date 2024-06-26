from django.db import models

from users.models import User


class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True,
        verbose_name="Фото")

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
