#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : getPartInfo.py
# Time       : 2023/4/27 9:17
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：查询零件数据
"""
import requests


def part_info_request(url, valid_cookies):
    # 要请求的url地址
    # url = 'http://127.0.0.1:8000/parts/' # 所有零信息
    # url = 'http://127.0.0.1:8000/parts/310000202010104689/' # 单个零件信息

    url = url
    # 设置请求头中的Cookie参数
    cookies = dict(cookies_are=valid_cookies)

    # 发送请求并获取响应
    response = requests.get(url, cookies=cookies)
    # 将获取到的数据解析为python字典
    part_info = response.json()

    # 查询所有零件数据
    # print(part_info)
    # print(type(part_info))  # 查看数据类型：list

    # 如果是单条查询打印响应的文本内容
    print('该零件的pid为：' + part_info['pid'])
    print('该零件的名字为：' + part_info['name'])
    print('该零件的单位为：' + part_info['unit'])
    print('该零件的库存量为：', part_info['amount'])
    print('该零件的单价为：', part_info['price'])
    print('该零件的储存地址为：' + part_info['store'])
    print('该零件的描述为：' + part_info['description'])


part_info_request('http://127.0.0.1:8000/parts/310000202010104689/', 'csrftoken=TAtQltwcrpcL6vU6dupCpWRsGtZ20y4X; '
                                                                     'sessionid=s5e34s8ns1yuhue0itb6a4l779ad5xtp;'
                                                                     'SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; '
                                                                     'SL_wptGlobTipTmp=1')
