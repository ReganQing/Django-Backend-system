#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : insertDataToMysql.py
# Description：通过语音输入向数据库中插入数据
"""
import re
import pymysql

# 创建数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="simple_erp",
    port=3306
)
cursor = conn.cursor()


# 定义文本匹配函数
def extract_data(text):

    # 提取pid
    pid_pattern = r'pid是(.*?)，'
    pid_match = re.search(pid_pattern, text)
    pid = pid_match.group(1)

    # 提取存储数量
    stock_pattern = r'库存量是(.*?)$'
    stock_match = re.search(stock_pattern, text)
    stock = stock_match.group(1)

    update_query = "UPDATE web_parts SET amount='%s' WHERE pid='%s'" % (stock, pid)
    cursor.execute(update_query)
    conn.commit()


# 示例用法
input_text = "更新零件信息，pid是820000198107177025，库存量是4211"
extract_data(input_text)

# 关闭数据库连接
cursor.close()
conn.close()
