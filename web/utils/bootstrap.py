#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : bootstrap.py
# Time       : 2023/4/17 13:32
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：form 格式 模块
"""


from django import forms


class BootStrap:
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段，给每个字段的插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            # 字段中有属性，保留原来的属性，没有属性才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = "请输入" + field.label

            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": "请输入" + field.label,
                    "autocomplete": "off"
                }


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


class BootStrapForm(BootStrap, forms.Form):
    pass

