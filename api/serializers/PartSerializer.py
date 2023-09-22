#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : PartSerializer.py
# Time       : 2023/4/25 14:52
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description： 零件列表信息的API序列化器，返回json信息
"""

from web.models import Parts
from rest_framework import serializers


# Serializer实现

class PartSerializer(serializers.Serializer):
    pid = serializers.CharField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=32)
    unit = serializers.CharField(required=False, allow_blank=True, max_length=32)
    amount = serializers.IntegerField(required=True, allow_null=True)
    price = serializers.IntegerField(required=True, allow_null=False)
    store = serializers.CharField(required=True, allow_blank=True, max_length=64)
    description = serializers.CharField(required=False, allow_blank=True, max_length=128)

    def create(self, validated_data):
        """ 根据经过验证的数据，创建并返回一个新的 `Parts` 实例 """
        return Parts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ 根据经过验证的数据，更新并返回现有的`Parts`实例 """
        instance.name = validated_data.get('name', instance.name)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.price = validated_data.get('price', instance.price)
        instance.store = validated_data.get('store', instance.store)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


# ModelSerializer实现

class PartsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = ['pid', 'name', 'unit', 'amount', 'price', 'store', 'description']


