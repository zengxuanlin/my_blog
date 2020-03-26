'''
@Author: your name
@Date: 2020-03-18 08:49:14
@LastEditTime: 2020-03-18 08:59:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /my_blog/server/utils.py
'''
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from models import User
from flask import request
import json
from secret_key import key
import uuid
# 根据token解析用户信息
def get_user(token):
    s = Serializer(key)
    try:
        data = s.loads(token)
    except:
        return None
    return User.query.filter_by(id=data['id']).first()


def post_json():
    data = request.get_data()
    return  json.loads(data.decode('utf-8'))


array = ["a", "b", "c", "d", "e", "f",
         "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
         "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
         "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
         "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]


def get_short_id():
    id = str(uuid.uuid4()).replace("-", '')
    buffer = []

    for i in range(0, 8):
        start = i * 4
        end = i * 4 + 4
        val = int(id[start:end], 16)
        buffer.append(array[val % 62])
    string = "".join(buffer)
    return 'zz'+string
