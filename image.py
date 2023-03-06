# -*- coding: utf-8 -*-

import aircv as ac
from PIL import Image, ImageDraw, ImageFont


def write():
    """
    在图片上写文字
    :return:
    """
    txt = "你这个死宅说话"
    txt2 = "   还挺搞笑的"
    font_img = Image.open("1.jpg")
    draw = ImageDraw.Draw(font_img)
    # 指定文字字体
    ttfront = ImageFont.truetype('./simhei.ttf', 20)
    draw.text((40, 60), txt, fill=(0, 0, 0), font=ttfront)
    draw.text((60, 130), txt2, fill=(0, 0, 0), font=ttfront)
    font_img.save("./out.jpg")


def imgCut(imgsrc, box, newimagename="cutting.jpg"):
    """
    图片裁剪，从图片上取得部分图片的内容（长方形区域）
    :param imgsrc:
    :param box:
    :param newimagename:
    :return:
    """
    im = Image.open(imgsrc)
    # box = (10,10,100,100)
    region = im.crop(box)
    region.save(newimagename)


def paste():
    """
    图片的拼合，2个图片拼合到成一个图片
    :return:
    """
    img = Image.open("1.jpg")
    jgz = Image.open("cutting.jpg")
    img.paste(jgz, (196, 139))
    img.save("./out.jpg")


def matchImg(imgsrc, imgobj, confidence=0.9):
    """
    查找图片在原始图片上的坐标点
    参考资料：https://www.cnblogs.com/meitian/p/7417582.html
    :param imgsrc:原始图像
    :param imgobj:待查找的图片
    :param confidence:
    :return:
    """
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)

    match_result = ac.find_template(imsrc, imobj,
                                    confidence)
    # sample: {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        # 添加图片的高和宽
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽

    return match_result


def find_all_template(imgsrc, imgobj, confidence=0.9):
    """
    查找图片在原始图片上的坐标点
    参考资料：https://www.cnblogs.com/meitian/p/7417582.html
    :param imgsrc:原始图像
    :param imgobj:待查找的图片
    :param confidence:
    :return:
    """
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)

    match_result = ac.find_all_template(imsrc, imobj,
                                        confidence)
    # sample：{'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    return match_result


def baidu_ai():
    """
    利用百度云识别图片中的文字
    :return:
    """
    from aip import AipOcr

    APP_ID = ''  # 百度云后台获取
    API_KEY = ''  # 百度云后台获取
    SECRET_KEY = ''  # 百度云后台获取

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content('out.jpg')

    """ 调用通用文字识别, 图片参数为本地图片 """
    return client.basicGeneral(image)


def get_file_content(filePath):
    """
    读取图片
    :param filePath:
    :return:
    """
    with open(filePath, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    result = find_all_template('0.jpg', '1.jpg')
    print(result)
