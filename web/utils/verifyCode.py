#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : verifyCode.py
# Time       : 2023/3/2 14:22
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：生成验证码文件
"""

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def check_code(width=120, height=30, char_length=5, font_file='ARLRDBD.TTF', font_size=28):
    code = []
    bg_img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(bg_img, mode='RGB')

    def rndChar():
        """
        生成随机字符
        :return:
        """
        return chr(random.randint(65, 90))
        # 数字
        # return str(random.randint(0, 9))

    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 255), random.randint(10, 255), random.randint(60, 255))

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text((i * width / char_length, h), char, font=font, fill=rndColor())

    # 画干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 画干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rndColor())
    re_img = bg_img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return re_img, "".join(code)


if __name__ == '__main__':
    img, code_str = check_code()
    print(code_str)

    with open('code.png', 'wb') as f:
        img.save(f, format='png')


