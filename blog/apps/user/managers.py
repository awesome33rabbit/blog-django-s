#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/12/10 21:21
# @File     : managers.py python3.9
# @Software : PyCharm blog-django
# @Desc     : TODO
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
import hashlib


class UserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)  # 给密码进行加密
        user.save()
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)
