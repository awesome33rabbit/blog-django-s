#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/12/17 17:45
# @File     : serializers.py python3.9
# @Software : PyCharm blog-django
# @Desc     : TODO

from rest_framework import serializers

from book.models import Book, Sale


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"

    def create(self, validated_data):
        book = validated_data["book"]
        count = validated_data["count"]

        sale, _ = Sale.objects.get_or_create(book=book, defaults={"count": 0})

        if count > book.count:
            raise ValueError("")
            # return sale

        sale.count += count
        book.count -= count
        sale.save()
        book.save()
        return sale
