#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : month_sale.py
# Time       : 2023/9/22 10:21
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description: 解析时间返回月度销售额和月度销售件数
"""


def month_sale(sale_info):
    # 数据初始化
    # 一月份
    jan_profit = 0
    jan_sale_num = 0
    # 二月份
    feb_profit = 0
    feb_sale_num = 0
    # 三月份
    mar_profit = 0
    mar_sale_num = 0
    # 四月份
    apr_profit = 0
    apr_sale_num = 0
    # 五月份
    may_profit = 0
    may_sale_num = 0
    # 六月份
    jun_profit = 0
    jun_sale_num = 0
    # 七月份
    jul_profit = 0
    jul_sale_num = 0
    # 八月份
    aug_profit = 0
    aug_sale_num = 0
    # 九月份
    sep_profit = 0
    sep_sale_num = 0
    # 十月份
    oct_profit = 0
    oct_sale_num = 0
    # 十一月份
    nov_profit = 0
    nov_sale_num = 0
    # 十二月份
    dec_profit = 0
    dec_sale_num = 0
    month_list = []
    for sale in sale_info:
        # 解析时间
        timestamp = sale.time
        month = timestamp.month

        for i in range(1, 13):
            month_list.append(i)
        # 开始计算月度销售情况
        if month == month_list[0]:
            jan_profit += sale.profit
            jan_sale_num += sale.sale_num
        elif month == month_list[1]:
            feb_profit += sale.profit
            feb_sale_num += sale.sale_num
        elif month == month_list[2]:
            mar_profit += sale.profit
            mar_sale_num += sale.sale_num
        elif month == month_list[3]:
            apr_profit += sale.profit
            apr_sale_num += sale.sale_num
        elif month == month_list[4]:
            may_profit += sale.profit
            may_sale_num += sale.sale_num
        elif month == month_list[5]:
            jun_profit += sale.profit
            jun_sale_num += sale.sale_num
        elif month == month_list[6]:
            jul_profit += sale.profit
            jul_sale_num += sale.sale_num
        elif month == month_list[7]:
            aug_profit += sale.profit
            aug_sale_num += sale.sale_num
        elif month == month_list[8]:
            sep_profit += sale.profit
            sep_sale_num += sale.sale_num
        elif month == month_list[9]:
            oct_profit += sale.profit
            oct_sale_num += sale.sale_num
        elif month == month_list[10]:
            nov_profit += sale.profit
            nov_sale_num += sale.sale_num
        elif month == month_list[11]:
            dec_profit += sale.profit
            dec_sale_num += sale.sale_num

    month_profit = [
        jun_profit,
        feb_profit,
        mar_profit,
        apr_profit,
        may_profit,
        jun_profit,
        jul_profit,
        aug_profit,
        sep_profit,
        oct_profit,
        nov_profit,
        dec_profit,
    ]
    month_sale_num = [
        jun_sale_num,
        feb_sale_num,
        mar_sale_num,
        apr_sale_num,
        may_sale_num,
        jun_sale_num,
        jul_sale_num,
        aug_sale_num,
        sep_sale_num,
        oct_sale_num,
        nov_sale_num,
        dec_sale_num,
    ]

    return month_profit, month_sale_num
