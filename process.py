# 图片处理相关

import requests
import hashlib
from PIL import Image
import os
from io import BytesIO

# 鉴定是否含有不良信息
def checkImg(imgPath):

    url = "https://eolink.o.apispace.com/nrsh/imgcheck"
    payload = "imageUrl=&BizType="
    headers = {
        "X-APISpace-Token": "",
        "Authorization-Type": "apikey",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, headers=headers, data=payload)

    # print(response.text)
    return True # 合法

def compress(imgPath, maxSize = 1024 * 1024, outputPath):
    img = Image.open(imgPath)
    imgSize = os.path.getsize(imgPath)
    if imgSize <= maxSize:
        img.save(outputPath)
        return
    imgByteArr = BytesIO()
    img.save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    imgByteArrLen = len(imgByteArr)
    while imgByteArrLen > maxSize:
        img = img.resize((int(img.size[0] * 0.9), int(img.size[1] * 0.9)))
        imgByteArr = BytesIO()
        img.save(imgByteArr, format='JPEG')
        imgByteArr = imgByteArr.getvalue()
        imgByteArrLen = len(imgByteArr)
    with open(outputPath, 'wb') as f:
        f.write(imgByteArr)

def generateThumbnail(imgPath, width = 200, height = 200, outputPath):
    img = Image.open(imgPath)
    img.thumbnail((width, height))
    img.save(outputPath)

def generateMD5(imgPath):
    with open(imgPath, 'rb') as f:
        md5 = hashlib.md5(f.read()).hexdigest()
    return md5

def generateKeywords(imgPath):
    return "keywords"

if __name__ == '__main__':
    checkImg("./exampleImg/ikun.jpg")