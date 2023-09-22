#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : parts.py
# Time       : 2023/4/18 9:47
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：零件管理
"""

from django.shortcuts import render, redirect
from web import models
from web.utils.pagination import Pagination
from web.utils.form import PartModelForm


def part_list(request):
    """获取零件数据"""
    # 设置搜索条件构造搜索
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["name__contains"] = search_data

    # 根据搜索条件获取数据
    queryset = models.Parts.objects.filter(**data_dict)

    page_obj = Pagination(request, queryset, page_size=10)

    context = {
        "query_set": page_obj.page_queryset,
        "page_string": page_obj.html(),
        "search_data": search_data,
    }

    return render(request, "part_list.html", context)


def part_add(request):
    """添加零件"""
    if request.method == "GET":
        form = PartModelForm()
        return render(request, "part_add.html", {"form": form})

    # 用户POST进行数据校验
    form = PartModelForm(data=request.POST)
    if form.is_valid():
        # 将数据保存到零件信息表中
        form.save()
        return redirect("/part/list/")

    # 若校验失败(在页面上显示错误信息)

    return render(request, "part_add.html", {"form": form})


def part_edit(request, nid):
    """编辑零件"""
    row_object = models.Parts.objects.filter(id=nid).first()

    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据(对象)
        form = PartModelForm(instance=row_object)
        return render(request, "part_edit.html", {"form": form})

    form = PartModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要在用户输入以外增加一点值
        # form.instance.字段名 = 值
        form.save()
        return redirect("/part/list/")
    return render(request, "part_edit.html", {"form": form})


def part_delete(request, nid):
    """零件删除"""
    models.Parts.objects.filter(id=nid).delete()
    return redirect("/part/list/")
