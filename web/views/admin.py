#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : admin.py
# Time       : 2023/2/28 14:23
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：管理员账户管理
"""

from django.shortcuts import render, redirect
from web import models
from web.utils.pagination import Pagination
from web.utils.form import AdminModelForm, AdminEditModelForm, AdminResetModelForm

# Register your models here.


def admin_list(request):
    """管理员列表"""
    # 获取当前登录用户session信息
    # info_dict = request.session.get("info")
    # print(info_dict["id"])
    # print(info_dict["name"])

    # 设置搜索条件构造搜索
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["user__contains"] = search_data

    # 根据搜索条件获取数据
    queryset = models.Admin.objects.filter(**data_dict)

    # 分页功能
    page_obiect = Pagination(request, queryset)
    context = {
        "queryset": page_obiect.page_queryset,
        "page_string": page_obiect.html(),
        "search_data": search_data,
    }
    return render(request, "admin_list.html", context)


def admin_add(request):
    """添加管理员"""
    title = "新建管理员"

    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "change.html", {"form": form, "title": title})

    # 获取用户发起的POST请求信息并进行数据验证
    form = AdminModelForm(data=request.POST)

    if form.is_valid():
        form.save()
        return redirect("/admin/list")

    return render(request, "change.html", {"form": form, "title": title})


def admin_edit(request, nid):
    """编辑管理员"""

    # 先作判断，判断nid是否存在于数据库中，如果不存在返回错误页面
    row_object = models.Admin.objects.filter(id=nid).first()
    # 如果数据不存在
    if not row_object:
        return render(request, "error.html", {"msg": "数据不存在"})

    title = "编辑管理员"

    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, "change.html", {"form": form, "title": title})

    # 获取用户发起的POST请求信息并进行数据验证
    form = AdminEditModelForm(data=request.POST, instance=row_object)

    if form.is_valid():
        form.save()
        return redirect("/admin/list")

    return render(request, "change.html", {"form": form, "title": title})


def admin_del(request, nid):
    """删除管理员"""
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/")


def admin_reset(request, nid):
    """重置密码"""
    # 先作判断，判断nid是否存在于数据库中，如果不存在返回错误页面
    row_object = models.Admin.objects.filter(id=nid).first()
    # 如果数据不存在
    if not row_object:
        return render(request, "error.html", {"msg": "数据不存在"})

    title = "重置管理员密码 - {}".format(row_object.user)
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, "change.html", {"form": form, "title": title})

    # 获取用户发起的POST请求信息并进行数据验证
    form = AdminResetModelForm(data=request.POST, instance=row_object)

    if form.is_valid():
        form.save()
        return redirect("/admin/list")

    return render(request, "change.html", {"form": form, "title": title})
