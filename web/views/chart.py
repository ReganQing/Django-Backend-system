#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : chart.py
# Time       : 2023/3/7 11:30
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：数据统计图表
"""
from django.shortcuts import render
from web import models
from web.middleWare.month_sale import month_sale
from web.middleWare.category_profit import category_profit


def chart_list(request):
    """数据统计"""

    # 获取销售数据
    sale_info = models.Sales.objects.all()
    # 客户市场细分销售额
    company_profit = 0
    business_profit = 0
    consumer_profit = 0
    # 总销售额
    total_profit = 0
    # 总销售件数
    total_products = 0
    for sale in sale_info:
        # 计算客户市场细分销售额
        if sale.customer == "COMPANY":
            company_profit += sale.profit
        elif sale.customer == "SMALL_BUSINESS":
            business_profit += sale.profit
        elif sale.customer == "CONSUMER":
            consumer_profit += sale.profit

        # 计算总销售额
        total_profit += sale.profit
        # 计算总件数
        total_products += sale.sale_num
    # 获取月度销售数据
    month_profit, month_sale_num = month_sale(sale_info)
    # 获取类别销售额
    categorys_profit = category_profit(sale_info)
    return render(
        request,
        "chart_list.html",
        {
            "company": "%.2f" % company_profit,
            "business": "%.2f" % business_profit,
            "consumer": "%.2f" % consumer_profit,
            "total_profit": "%.2f" % total_profit,
            "total_products": total_products,
            "month_profit": month_profit,
            "month_sale_num": month_sale_num,
            "category_profit": categorys_profit,
        },
    )
