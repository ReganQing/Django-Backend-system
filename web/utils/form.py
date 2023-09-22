#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : form.py
# Time       : 2023/4/17 13:46
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：form 模块
"""
from django import forms
from web import models
from web.utils.encrypt import md5
from django.core.validators import ValidationError

from web.utils.bootstrap import BootStrapModelForm


class DepartmentModelForm(BootStrapModelForm):
    class Meta:
        model = models.Department
        fields = ["department_name", "employees_num"]

    # 重新定义类实例化后初始化的方法，super表示执行父类的方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 循环找到所有的插件，添加class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": "请输入" + field.label,
            }


class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "age", "create_time", "gender", "depart"]

    # 重新定义类实例化后初始化的方法，super表示执行父类的方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 循环找到所有的插件，添加class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": "请输入" + field.label,
            }


# class NumAddModelForm(BootStrapModelForm):
#     # 如果想让手机号不可修改，则添加以下语句
#     # mobile = forms.CharField(disabled=True, label="手机号")
#
#     # 校验方式1： 正则+字段
#     # mobile = forms.CharField(
#     #     label="手机号",
#     #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错位')],
#     # )
#
#     class Meta:
#         model = models.PartsNumber
#         fields = ['mobile', 'price', 'level', 'status']
#
#     # 重新定义类实例化后初始化的方法，super表示执行父类的方法
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         # 循环找到所有的插件，添加class="form-control"
#         for name, field in self.fields.items():
#             field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}
#
#     # 校验方式2：钩子方法
#     def clean_mobile(self):
#         txt_mobile = self.cleaned_data["mobile"]
#         exist = models.PartsNumber.objects.filter(mobile=txt_mobile).exists()
#         if len(txt_mobile) != 11:
#             # 验证不通过，抛出错误
#             raise ValidationError("手机号格式错误")
#         elif exist:
#             raise ValidationError("手机号已存在")
#         # 验证通过返回用户输入的值
#         return txt_mobile
#
#
# class NumEditModelForm(BootStrapModelForm):
#     # 如果想让手机号不可修改，则添加以下语句
#     # mobile = forms.CharField(disabled=True, label="手机号")
#     # 校验方式1： 正则+字段
#     # mobile = forms.CharField(
#     #     label="手机号",
#     #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错位')],
#     # )
#
#     class Meta:
#         model = models.PartsNumber
#         fields = ['mobile', 'price', 'level', 'status']
#
#     # 重新定义类实例化后初始化的方法，super表示执行父类的方法
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         # 循环找到所有的插件，添加class="form-control"
#         for name, field in self.fields.items():
#             field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}
#
#     # 在编辑手机号进行重复验证时，需要排除自身
#     def clean_mobile(self):
#
#         txt_mobile = self.cleaned_data["mobile"]
#         exist = models.PartsNumber.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
#         if len(txt_mobile) != 11:
#             # 验证不通过，抛出错误
#             raise ValidationError("手机号格式错误")
#         elif exist:
#             raise ValidationError("手机号已存在")
#         # 验证通过返回用户输入的值
#         return txt_mobile


class AdminModelForm(BootStrapModelForm):
    confirm_pwd = forms.CharField(
        label="确认密码", widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["user", "password", "confirm_pwd"]
        widgets = {"password": forms.PasswordInput(render_value=True)}

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_pwd(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_pwd"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段就保存到数据库
        return confirm


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ["user"]


class AdminResetModelForm(BootStrapModelForm):
    confirm_pwd = forms.CharField(
        label="确认密码", widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_pwd"]
        widgets = {"password": forms.PasswordInput(render_value=True)}

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和新输入的密码一致
        exists = models.Admin.objects.filter(
            id=self.instance.pk, password=md5_pwd
        ).exists()
        if exists:
            raise ValidationError("密码不能与原密码一致")

        return md5_pwd

    def clean_confirm_pwd(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_pwd"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段就保存到数据库
        return confirm


# 零件表
class PartModelForm(BootStrapModelForm):
    class Meta:
        model = models.Parts
        fields = ["pid", "name", "unit", "amount", "price", "store", "description"]


class PartEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Parts
        fields = ["pid", "name", "unit", "amount", "price", "store", "description"]
