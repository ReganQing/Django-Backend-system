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
    # 提取"LED灯"
    name_pattern = r'名字是(.*?)，'
    name_match = re.search(name_pattern, text)
    name = name_match.group(1)

    # 提取"211111"
    pid_pattern = r'pid是(.*?)$'
    pid_match = re.search(pid_pattern, text)
    pid = pid_match.group(1)

    delete_query = "DELETE FROM web_parts where name='%s' and pid='%s'" % (name, pid)
    cursor.execute(delete_query)
    conn.commit()


# 示例用法
# input_text = Conversation.doConverse(fp)  # 得到语音识别后的文本
input_text = "删除零件信息，名字是LED灯，pid是211111"
extract_data(input_text)

# 关闭数据库连接
cursor.close()
conn.close()
