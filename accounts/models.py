from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, name, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, name=name, **extra_fields)
        user.set_password(password)
        return user.save()

    def create_superuser(self, username, email, password, name, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(username, email, password, name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, validators=[UnicodeUsernameValidator()])
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=20)
    penalty_date = models.DateField(null=True)
    is_admin = models.BooleanField(default=False)

    @property
    def can_borrow(self):
        if self.penalty_date is None or self.penalty_date < datetime.now():
            self.penalty_date = None
            return True
        return False

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']
    objects = UserManager()
