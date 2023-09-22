#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : partsAPI.py
# Time       : 2023/4/25 15:46
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：用Serializer来写一个Django视图
"""
from web.models import Parts
from api.serializers.PartSerializer import PartsModelSerializer
# from rest_framework import generics

# from rest_framework import mixins

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class PartsList(APIView):
    """列出所有零件信息，或者创建一个新零件"""

    def get(self, request, format=None):
        parts_info = Parts.objects.all()
        serializer = PartsModelSerializer(parts_info, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PartsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartsDetail(APIView):
    """" 获取，更新，删除Part """

    def get_object(self, pid):
        try:
            return Parts.objects.get(pid=pid)
        except Parts.DoesNotExist:
            raise Http404

    def get(self, request, pid, format=None):
        part = self.get_object(pid)
        serializer = PartsModelSerializer(part)
        return Response(serializer.data)

    def put(self, request, pid, format=None):
        part = self.get_object(pid)
        serializer = PartsModelSerializer(part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pid, format=None):
        part = self.get_object(pid)
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 使用mixins


"""class PartsList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartsModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PartsDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartsModelSerializer

    def get(self, request, *args, **kargs):
        return self.retrieve(request, *args, **kargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)"""

# 使用基于类的通用视图

"""class PartsList(generics.ListCreateAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartsModelSerializer


class PartsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartsModelSerializer"""
