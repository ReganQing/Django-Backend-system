#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : user.py
# Time       : 2023/2/28 13:52
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：用户信息管理
"""

from django.shortcuts import render, redirect
from web import models
from web.utils.pagination import Pagination
from web.utils.form import UserModelForm

# Create your views here.


def user_list(request):
    # 获取用户数据
    user_info = models.UserInfo.objects.all()

    page_obj = Pagination(request, user_info, page_size=2)

    context = {
        "query_set": page_obj.page_queryset,
        "page_string": page_obj.html(),
    }
    return render(request, "user_list.html", context)


def user_add(request):
    """添加用户"""
    if request.method == "GET":
        context1 = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_info': models.Department.objects.all()
        }

        return render(request, "user_add.html", context1)

    user = request.POST.get('name')
    pwd = request.POST.get('password')
    age = request.POST.get('age')
    account = request.POST.get('account')
    ctime = request.POST.get('create_time')
    gender = request.POST.get('gender')
    depart = request.POST.get('depart')

    models.UserInfo.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=ctime,
                                   gender=gender, depart_id=depart)
    return redirect("/user/list/")


def user_add_model_form(request):
    """基于model form添加用户"""

    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_add_model_form.html', {"form": form})

    # 用户POST进行数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 将数据保存到用户信息表中
        form.save()
        return redirect("/user/list/")

    # 若校验失败(在页面上显示错误信息)

    return render(request, "user_add_model_form.html", {"form": form})


def user_edit(request, nid):
    """编辑用户"""
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据(对象)
        form = UserModelForm(instance=row_object)
        return render(request, "user_edit.html", {"form": form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要在用户输入以外增加一点值
        # form.instance.字段名 = 值
        form.save()
        return redirect("/user/list/")
    return render(request, "user_edit.html", {"form": form})


def user_del(request, nid):
    """用户删除"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
