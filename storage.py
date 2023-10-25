# 储存服务相关

import requests
import time
import config
import hashlib

def randomString(length=16):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def xuehai(file, md5):
    url = "https://filesoss.yunzuoye.net/XHFileServer/file/upload/CA107011/"
    payload = {}
    files=[
        ('files',(randomString() + '.jpg', file, 'image/jpeg')),
    ]
    headers = {
        'XueHai-MD5': md5,
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return (response.json())["uploadFileDTO"]["fileId"]

def upload(path):
    with open(path, 'rb') as f:
        md5 = hashlib.md5(f.read()).hexdigest()
    # 上传至学海OSS
    with open(path, 'rb') as f:
        fileId = xuehai(f, md5)
    return fileId

if __name__ == '__main__':
    fileId = upload("./exampleImg/ikun.jpg")
    print(fileId)