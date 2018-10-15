# -*- coding: utf-8 -*-

from aip import AipOcr
from PIL import Image

import re

APP_ID = '14405891'
API_KEY = 'tanseQfGI8w8eCU1ef61Mw6l'
SECRET_KEY = 'AxBFOjikG4FoewD2AYvyqOVRjHzlVDzC'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('out.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image);

print (result)

#""" 如果有可选参数 """
#options = {}
#options["language_type"] = "CHN_ENG"
#options["detect_direction"] = "true"
#options["detect_language"] = "true"
#options["probability"] = "true"
#
#""" 带参数调用通用文字识别, 图片参数为本地图片 """
#client.basicGeneral(image, options)
#
#url = "https//www.x.com/sample.jpg"
#
#""" 调用通用文字识别, 图片参数为远程url图片 """
#client.basicGeneralUrl(url);
#
#""" 如果有可选参数 """
#options = {}
#options["language_type"] = "CHN_ENG"
#options["detect_direction"] = "true"
#options["detect_language"] = "true"
#options["probability"] = "true"
#
#""" 带参数调用通用文字识别, 图片参数为远程url图片 """
#client.basicGeneralUrl(url, options)

