#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : auth.py
# Time       : 2023/3/2 9:22
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：中间件判断是否已登录
"""

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):
    """中间件1"""

    def process_request(self, request):
        # 0.排除那些不需要登录就可以访问的页面
        if request.path_info in ["/login/", "/image/code/"]:
            return

        # 1.读取当前访问的用户的session信息，如果能读到，说明已登录，就可以继续向后走。
        info_dict = request.session.get("info")
        if info_dict:
            return

        # 没有登陆则重新回到登陆页面
        return redirect("/login/")
        # 如果没有返回值（返回none），继续向后走
        # 如果有返回值，HttpResponse、render、redirect,则不再继续向后执行
        # return HttpResponse("无权访问")
