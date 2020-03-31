'''
@Author: your name
@Date: 2020-03-17 17:04:44
@LastEditTime: 2020-03-19 09:09:42
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /my_blog/server/models.py
'''
from ext import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from secret_key import key
import datetime
# 用户


class User(db.Model):
    __tablename__ = 'users'
    guid = str(uuid.uuid4()).replace('-', '')
    id = db.Column(db.String(64), primary_key=True, default=guid)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(255))
    age = db.Column(db.String(16), default=None)
    sex = db.Column(db.String(16), default=None)
    address = db.Column(db.String(64), default=None)
    nickName = db.Column(db.String(64), default=None)
    avatar = db.Column(db.Text, default=None)
    sign = db.Column(db.Text, default=None)
    createTime = db.Column(db.DateTime, default=datetime.datetime.now)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    articles = db.relationship('Article', backref='articles')
    home_id = db.Column(db.String(255),default=None)
    def __init__(self, username, password, role_id,home_id):
        self.username = username
        # 加密
        self.password = generate_password_hash(password)
        self.role_id = role_id
        self.home_id = home_id

    # 检查密码
    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    # 生成token
    def create_token(self, expiration=6000):
        print(key)
        s = Serializer(key, expires_in=expiration)
        return s.dumps({'id': self.id}).decode("ascii")
    #返回个人资料
    def to_dict(self):
        t = self.__dict__
        del t['_sa_instance_state']
        del t['password']
        del t['username']
        del t['role_id']
        del t['id']
        return t
# 角色表


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    roleName = db.Column(db.String(16), unique=True)

    def __init__(self, rn):
        self.roleName = rn

# 文章表


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.String(64), db.ForeignKey('users.id'))
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    time = db.Column(db.DateTime, default=datetime.datetime.now,
                     onupdate=datetime.datetime.now)
    mdText = db.Column(db.Text)

    def __init__(self, author_id, title, content, mdText):
        self.author_id = author_id
        self.title = title
        self.content = content
        self.mdText = mdText

    def to_dict(self):
        t = self.__dict__
        del t['_sa_instance_state']
        return t
# 评论


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    fromId = db.Column(db.Integer, db.ForeignKey('article.id'))
    name = db.Column(db.String(64))
    content = db.Column(db.String(64))
    time = db.Column(db.DateTime, default=datetime.datetime.now,
                     onupdate=datetime.datetime.now)
    comments = db.relationship('Article', backref='art')

    def __init__(self, fromId, name, content):
        self.fromId = fromId
        self.name = name
        self.content = content

    def to_dict(self):
        t = self.__dict__
        del t['_sa_instance_state']
        return t
