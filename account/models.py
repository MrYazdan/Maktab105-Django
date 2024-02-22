from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager ,BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError("Phone number must be set ...")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):

        extra_fields.update({
            'is_staff': True,
            'is_superuser': True,
            'is_active': True,
        })

        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = None

    phone = models.CharField(max_length=11, unique=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def username(self):
        return self.phone
