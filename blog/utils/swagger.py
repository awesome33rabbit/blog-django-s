#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/12/5 22:14
# @File     : swagger.py python3.9
# @Software : PyCharm blog-django
# @Desc     : TODO
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework import permissions


class AutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        tags = self.overrides.get("tags", None) or getattr(self.view, "tags", [])
        if not tags:
            tags = [operation_keys[0]]

        return tags


schema_view = get_schema_view(
    openapi.Info(
        title="个人博客",
        default_version="0.0.0",
        description="描述"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=OpenAPISchemaGenerator
)
