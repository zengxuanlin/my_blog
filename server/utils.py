from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from models import User
from flask import request
import json
from secret_key import key
# 根据token解析用户信息
def get_user(token):
    s = Serializer(key)
    try:
        data = s.loads(token)
    except:
        return None
    return User.query.filter_by(id=data['id']).first()


def post_json():
    data = request.get_data(as_text=True)
    return  json.loads(data)
