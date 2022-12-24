#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/12/5 21:56
# @File     : routers.py python3.9
# @Software : PyCharm blog-django
# @Desc     : TODO

from rest_framework import routers

from .views import BookViews, SaleViews

router = routers.SimpleRouter()

router_list = [
    (r"book", BookViews),
    (r"sale", SaleViews),
]

for i in router_list:
    router.register(*i)

urlpatterns = router.urls
