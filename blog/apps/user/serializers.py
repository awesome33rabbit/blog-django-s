#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderChaos
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/12/10 21:14
# @File     : serializers.py python3.9
# @Software : PyCharm blog-django
# @Desc     : TODO
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = []
        # exclude = ["password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        return instance
