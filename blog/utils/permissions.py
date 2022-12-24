#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/12/17 17:13
# @File     : permissions.py python3.9
# @Software : PyCharm blog-django
# @Desc     : TODO
from rest_framework.permissions import BasePermission


class MyIsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
