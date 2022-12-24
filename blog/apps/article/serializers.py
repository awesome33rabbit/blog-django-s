#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/12/5 21:42
# @File     : serializers.py python3.9
# @Software : PyCharm blog-django
# @Desc     : TODO

from rest_framework import serializers

from .models import ArticleCategory, ArticleTag, Article


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = "__all__"


# class ArticleTagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArticleTag
#         fields = "__all__"

class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        # depth = 3


class ArticleDetailSerializer(ArticleSerializer):
    class Meta:
        model = Article
        # fields = ["id", "title", "category"]
        fields = "__all__"
        # depth = 2

    # category = ArticleCategory

    # def get_category(self, obj):
    #     return obj.category.name + obj.category.desc


class CustomBookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.FloatField()
