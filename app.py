from flask_cors import *
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dbConfig import getUrl
from flask_cors import CORS
from blog_api import blog

from ext import db
from models import *
from secret_key import key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getUrl()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = key
db.init_app(app)
CORS(app,support_credentials=True)

with app.app_context():
    pass
    # db.drop_all()
    # db.create_all()
    # r1 = Role('管理员')
    # r2 = Role('用户')
    # db.session.add_all([r1,r2])
    # db.session.commit()
    # test_user = User('qwedsa123','567984','27','贵州省贵阳市','神的孩子都在跳舞',r1.id)
    # db.session.add(test_user)
    # db.session.commit()

    # c = Article(test_user.id,'今晚','很难受啊哈哈哈哈')
    # db.session.add(c)
    # db.session.commit()

    # common1 = Comment(c.id,'一位没姓名的网友','支持楼主~~~',)
    # common2 = Comment(c.id,'压缩','支持楼主~~~')
    # db.session.add_all([common1,common2])
    # db.session.commit()



print('数据库地址::',getUrl())



if __name__ == "__main__":
    app.register_blueprint(blog)
    app.run(debug=True)
