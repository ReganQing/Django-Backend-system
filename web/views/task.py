#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : task.py
# Time       : 2023/3/2 16:18
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：ajax学习
"""
import json
from django import forms
from django.shortcuts import render,  HttpResponse
from web.utils.pagination import Pagination
from django.views.decorators.csrf import csrf_exempt

from web import models
from web.utils.bootstrap import BootStrapModelForm


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.AjaxTask
        fields = "__all__"
        widgets = {
            # "detail": forms.Textarea  # 可以是Textarea, 也可以是小一些的TextInput
            "detail": forms.TextInput
        }


def ajax_task(request):
    """ 任务列表 """
    # 去数据库获取所有任务
    queryset = models.AjaxTask.objects.all().order_by("-id")
    page_object = Pagination(request, queryset)
    form = TaskModelForm()

    context = {
        'form': form,
        'queryset': page_object.page_queryset,  # 分完页的数据
        'page_string': page_object.html(),      # 生成的页数
    }

    return render(request, 'task_list.html', context)


@csrf_exempt
def ajax_list(request):
    print(request.GET)
    print(request.POST)
    data_dict = {"status": True, 'data': [11, 22, 33, 44]}
    js_string = json.dumps(data_dict)
    return HttpResponse(js_string)


@csrf_exempt
def ajax_add(request):
    # <QueryDict: {'level': ['1'], 'title': ['123'], 'detail': ['124'], 'user': ['1']}>
    # print(request.POST)

    # 1.对用户发过来的数据进行校验（Modelform进行校验）
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
