# 每个用户id，生成一个token，存入db
# 用户上传图片时，需要携带token，验证token是否有效
# 验证token有效，接收图片
# 图片处理：
# 1. 保存图片
# 2. 鉴定是否为合法图片
# 3. 生成缩略图，压缩原图至一定大小
# 4. 生成md5
# 5. 使用ai生成描述关键词
# 6. 多端储存图片
# 7. 保存图片元信息到db
# 8. 删除本地图片
# 返回图片信息

import os
import sys
import time
import json
import hashlib

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

