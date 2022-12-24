#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/12/10 21:15
# @File     : routers.py python3.9
# @Software : PyCharm blog-django
# @Desc     : TODO

from rest_framework import routers

from user.views import UserViews

router = routers.SimpleRouter()

router_list = [
    (r"user", UserViews),
]

for i in router_list:
    router.register(*i)

urlpatterns = router.urls
