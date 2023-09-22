#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : urls.py
# Time       : 2023/4/25 16:32
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：
"""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import partsAPI

urlpatterns = [
    path('parts/', partsAPI.PartsList.as_view()),
    path('parts/<int:pid>/', partsAPI.PartsDetail.as_view()),
    # path('users/', partsAPI.UserList.as_view()),
    # path('users/<int:id>/', partsAPI.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
