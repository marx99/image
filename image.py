# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import aircv as ac
import cv2
import numpy as np
from matplotlib import pyplot as plt

#在图片上写文字
def write():
    txt = "你这个死宅说话"
    txt2 = "   还挺搞笑的"
    font_img = Image.open("a2afcc6134a85edfdd475f6845540923df5475d5.jpg")
    draw = ImageDraw.Draw(font_img)
    ttfront = ImageFont.truetype('./simhei.ttf',20)
    draw.text((40,60),txt, fill=(0,0,0), font=ttfront)
    draw.text((60,130),txt2, fill=(0,0,0), font=ttfront)
    font_img.save("./out.jpg")
    
#裁剪
def imgCut(imgsrc,box,newimagename="cutting.jpg"):
    im = Image.open(imgsrc)
    #box = (10,10,100,100)
    region = im.crop(box)
    region.save(newimagename)

#图片的拼合
def paste():
    img = Image.open("a2afcc6134a85edfdd475f6845540923df5475d5.jpg")
    jgz = Image.open("cutting.jpg")
    img.paste(jgz,(196,139))
    img.save("./out.jpg")    

#查找图片在原始图片上的坐标点
#https://www.cnblogs.com/meitian/p/7417582.html
def matchImg(imgsrc,imgobj,confidence=0.9):#imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
 
    match_result = ac.find_template(imsrc,imobj,confidence)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])#0为高，1为宽

    return match_result

def find_all_template(imgsrc,imgobj,confidence=0.9):#imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
 
    match_result = ac.find_all_template(imsrc,imobj,confidence)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
#    if match_result is not None:
#        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])#0为高，1为宽

    return match_result


#paste()
#im1 = "1f77a900213fb80e4ac8c09c3ad12f2eb83894fb.jpg"
#im2 = "cutting.jpg"
#result = matchImg(im1,im2)
#print(result)
#    
#点赞处的icon    
#imgCut('wechat.jpg',(620,585,672,622),'1.jpg')
#时间
#imgCut('wechat.jpg',(110,585,212,622),'time.jpg')  
    
result  = find_all_template('wechat.jpg', 'time.jpg')
print(result)