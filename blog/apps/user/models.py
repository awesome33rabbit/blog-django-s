from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from user.managers import UserManager


# class Role(models.Model):
#     name = models.CharField("身份名称", max_length=16)


# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None

    # role = models.ForeignKey(Role, on_delete=models.CASCADE)
    # email = models.EmailField('email address', unique=True, blank=True)

    # USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    date_joined = models.DateTimeField("加入日期", auto_now_add=True)

    # date_update = models.DateTimeField("最近登陆", auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.__class__.__name__}({self.username})"

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name
