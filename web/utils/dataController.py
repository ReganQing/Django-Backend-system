#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : dataController.py
# Time       : 2023/8/5 9:23
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：
"""
# -*- coding: utf-8 -*-
# 数据库操作插件
import re
import pymysql
from robot import config, logging
from robot.sdk.AbstractPlugin import AbstractPlugin

logger = logging.getLogger(__name__)


class Plugin(AbstractPlugin):
    """数据库操作"""
    SLUG = "database_controller"

    def __init__(self, arg):
        super(Plugin, self).__init__()
        self.arg = arg

    def insertDataToDatabase(text):
        """新增零件信息"""
        # 得到文本里包含的信息
        name = getPartName(text)

        pid = getPid(text)
        unit = getUnit(text)
        amount = getStoreNum(text)
        price = getPrice(text)
        store = getAddress(text)
        description = getDescription(text)
        insert_query = "INSERT INTO web_parts (pid, name, unit, amount, price, store, description) " \
                       "VALUE (%s, %s, %s, %s, %s, %s, %s)"

        return insert_query


    def updateData(text):
        """更新零件信息"""
        pid = getPid(text)

        # 提取零件库存数量
        stock_pattern = r'库存量是(.*?)$'
        stock_match = re.search(stock_pattern, text)
        stock = stock_match.group(1)

        update_query = "UPDATE web_parts SET amount='%s' WHERE pid='%s'" % (stock, pid)
        return update_query


    def deleteData(text):
        """删除零件信息"""
        name = getPartName(text)
        """提取零件PID号"""
        pid_pattern = r'pid是(.*?)$'
        pid_match = re.search(pid_pattern, text)
        pid = pid_match.group(1)

        delete_query = "DELETE FROM web_parts where name='%s' and pid='%s'" % (name, pid)
        return delete_query


    def getPartName(text):
        """提取零件名称"""
        name_pattern = r'名字是(.*?)，'
        name_match = re.search(name_pattern, text)
        name = name_match.group(1)
        return name


    def getPid(text):
        """提取零件PID号"""
        pid_pattern = r'pid是(.*?)，'
        pid_match = re.search(pid_pattern, text)
        pid = pid_match.group(1)
        return pid


    def getPrice(text):
        """提取零件单价"""
        price_pattern = r'单价是(.*?)元，'
        price_match = re.search(price_pattern, text)
        price = price_match.group(1)
        return price


    def getStoreNum(text):
        """提取零件库存数量"""
        stock_pattern = r'库存量是(.*?)，'
        stock_match = re.search(stock_pattern, text)
        stock = stock_match.group(1)
        return stock


    def getUnit(text):
        """提取零件单位"""
        unit_pattern = r'计量单位是(.*?)，'
        unit_match = re.search(unit_pattern, text)
        unit = unit_match.group(1)
        return unit


    def getAddress(text):
        """提取零件库存地址"""
        address_pattern = r'存储地址为(.*?)，'
        address_match = re.search(address_pattern, text)
        address = address_match.group(1)
        return address


    def getDescription(text):
        """提取零件附加描述"""
        description_pattern = r'附加描述为(.*?)$'
        description_match = re.search(description_pattern, text)
        description = description_match.group(1)
        return description


    def handle(self, text, parsed):
        # 检查数据库配置
        profile = config.get()
        if self.SLUG not in profile or \
                'host' not in profile[self.SLUG] or \
                'user' not in profile[self.SLUG] or \
                'password' not in profile[self.SLUG] or \
                'database' not in profile[self.SLUG] or \
                'port' not in profile[self.SLUG]:
            self.say(u"数据库配置有误，请检查配置", cache=True)
            return

        # 创建数据库连接
        conn = pymysql.connect(
            host=profile[self.SLUG]["host"],
            user=profile[self.SLUG]["user"],
            password=profile[self.SLUG]["password"],
            database=profile[self.SLUG]["database"],
            port=profile[self.SLUG]["port"]
        )
        cursor = conn.cursor()
        try:
            if self.nlu.hasIntent(parsed, 'DATABASE_INSERT'):
                values = (pid, name, unit, amount, price, store, description)
                cursor.execute(insertDataToDatabase(text), values)
                conn.commit()
                self.say(u'数据已插入', cache=True)
            elif self.nlu.hasIntent(parsed, 'UPDATA_DATA'):
                cursor.execute(updataData(text))
                conn.commit()
                self.say(u'数据已更新', cache=True)
            elif self.nlu.hasIntent(parsed, 'DELETE_DATA'):
                cursor.execute(deleteData(text))
                conn.commit()
                self.say(u'数据已删除', cache=True)

            # 关闭数据库连接
            cursor.close()
            conn.close()

        except Exception as e:
            logger.error(e)
            self.say(u'抱歉，数据库操作失败，请检查相关配置', cache=True)


    def isValid(self, text, parsed):
        return any(word in text for word in [u"插入零件数据", u"存储零件信息", u"存储零件数据", u"新增零件数据",
                                             u"删除零件信息", u"清空零件信息", u"删掉零件数据", u"消除零件数据",
                                             u"修改零件信息", u"更新零件信息", u"修改零件数据", u"更新零件数据"])
