#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : category_profit.py
# Time       : 2023/9/22 14:14
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：计算各类产品销售额及销售数量
"""


def category_profit(sale_info):
    # 数据初始化
    corkscrew_profit = 0
    arm_profit = 0
    rheostat_profit = 0
    wheel_profit = 0
    motor_profit = 0
    bearing_profit = 0
    base_profit = 0

    # 计算类别利润
    for sale in sale_info:
        if sale.name_id == "1":
            corkscrew_profit += sale.profit
        elif sale.name_id == "2":
            arm_profit += sale.profit
        elif sale.name_id == "3":
            rheostat_profit += sale.profit
        elif sale.name_id == "4":
            wheel_profit += sale.profit
        elif sale.name_id == "5":
            motor_profit += sale.profit
        elif sale.name_id == "6":
            bearing_profit += sale.profit
        elif sale.name_id == "7":
            base_profit += sale.profit

    category_profit_list = [
        corkscrew_profit,
        arm_profit,
        rheostat_profit,
        wheel_profit,
        motor_profit,
        bearing_profit,
        base_profit,
    ]

    return category_profit_list
