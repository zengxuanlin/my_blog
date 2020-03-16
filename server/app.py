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
    # test_user = User('qwedsa123','567984',r1.id)
    # db.session.add(test_user)
    # db.session.commit()



print('数据库地址::',getUrl())



if __name__ == "__main__":
    app.register_blueprint(blog)
    app.run(debug=True)
