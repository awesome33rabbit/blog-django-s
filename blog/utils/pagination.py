#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/12/5 22:29
# @File     : pagination.py python3.9
# @Software : PyCharm blog-django
# @Desc     : TODO

from rest_framework.pagination import PageNumberPagination as DRFPageNumberPagination


class PageNumberPagination(DRFPageNumberPagination):
    page_size_query_param = "size"
