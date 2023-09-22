#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : account.py
# Time       : 2023/3/1 20:09
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：账户管理
"""
from django.shortcuts import render, redirect, HttpResponse
from django import forms

from io import BytesIO

from web import models
from web.utils.encrypt import md5
from web.utils.bootstrap import BootStrapForm
from web.utils.verifyCode import check_code


class LoginForm(BootStrapForm):
    user = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
    )
    verify_code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功，获取到用户名和密码
        # 验证码的校验
        user_input_code = form.cleaned_data.pop('verify_code')  # 把验证码从cleaned_data中剔除
        verify_code = request.session.get('image_code', '')
        if verify_code.upper() != user_input_code.upper():
            form.add_error("verify_code", "验证码错误")
            return render(request, 'login.html', {'form': form})

        # 去数据库校验用户名和密码是否正确，获取用户对象， 如果正确返回的是None
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            # 主动在固定位置添加错误提示
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        # 用户名和密码正确
        # 网站生成随机字符串；写到用户浏览器的cookie中；再写入到session;
        request.session["info"] = {'name': admin_object.user}
        # session 有效期
        request.session.set_expiry(60 * 60 * 24 * 30 * 6)    # 半年
        return redirect('/part/list/')

    return render(request, 'login.html', {'form': form})


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect('/login/')


def image_code(request):
    """生成图片验证码"""
    # 调用pillow函数，生成图片
    img, code_str = check_code()

    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_str
    # 给session加上超时机制，3分钟
    request.session.set_expiry(60 * 3)
    print(code_str)

    stream = BytesIO()
    img.save(stream, "png")

    return HttpResponse(stream.getvalue())
