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
    # pattern = r'存储零件信息，名字是(.+?)，pid是(\d+?)，单价是(\d+?)元，库存量是(\d+?)，计量单位是(.+?)，存储地址为(.+?)，附加描述为(.+?)$'
    pattern = (r'(?:名字|产品名|物品名称)是(.+?)(?:pid|产品ID|物品ID)是(\d+?)(?:单价|价格)是(\d+?)元(?:，库存量是(\d+?))?(?:，计量单位是(.+?))?('
               r'?:存储地址为(.+?))?(?:附加描述为(.+))?')

    match = re.search(pattern, text)
    if match:
        name = match.group(1)
        pid = match.group(2)
        unit = match.group(5)
        amount = match.group(4)
        price = match.group(3)
        store = match.group(6)
        description = match.group(7)

        # 存储到数据库
        insert_query = "INSERT INTO web_parts (pid, name, unit, amount, price, store, description) " \
                       "VALUE (%s, %s, %s, %s, %s, %s, %s)"
        values = (pid, name, unit, amount, price, store, description)
        cursor.execute(insert_query, values)
        conn.commit()

        print("数据已存储到数据库。")
    else:
        print("未找到匹配的数据。")


def clean_and_correct_text(text):
    # 删除特殊字符和标点符号
    text = re.sub(r'[!@#$%^&*()\[\]{};:,.<>?/|~_]', '', text)

    # 替换常见错误符号
    text = text.replace('，', ',')
    text = text.replace('。', '.')
    # 可以根据需要添加其他符号的替换规则

    # 纠正换行符和空格
    text = re.sub(r'\s+', ' ', text)

    # 转换为小写
    text = text.lower()

    # 修复常见词汇错误
    # 这部分需要根据具体需求添加词汇修复规则

    return text


# 示例用法
# input_text = Conversation.doConverse(fp)  # 得到语音识别后的文本
input_text = "存储零件信息，名字是LED灯，pid是288，单价是45元，库存量是3675，计量单位是件，存储地址为仓库B，附加描述为哈哈哈哈哈"
cleaned_text = clean_and_correct_text(input_text)
print(cleaned_text)

extract_data(input_text)

# 关闭数据库连接
cursor.close()
conn.close()
