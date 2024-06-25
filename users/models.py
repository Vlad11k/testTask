from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # first_name = models.CharField(verbose_name='first name', max_length=150, blank=True)
    # last_name = models.CharField(verbose_name='last name', max_length=150, blank=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        blank=True
    )
    phone = models.CharField(
        verbose_name='phone',
        min_length=9,
        max_length=100,
        unique=True,
        blank=True)
    full_name = models.CharField(
        verbose_name='first name',
        max_length=150,
        blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
