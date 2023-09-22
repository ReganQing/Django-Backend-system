#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : encrypt.py
# Time       : 2023/4/17 14:59
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：
"""
import hashlib
from django.conf import settings


def md5(data_string):

    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()