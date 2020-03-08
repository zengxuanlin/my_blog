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
    username = db.Column(db.String(16))
    password = db.Column(db.String(255))
    age = db.Column(db.String(3))
    address = db.Column(db.String(64))
    nickName = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    articles = db.relationship('Article', backref='articles')

    def __init__(self, username, password, age, address, nick, role_id):
        self.username = username
        # 加密
        self.password = generate_password_hash(password)
        self.age = age
        self.address = address
        self.nickName = nick
        self.role_id = role_id

    # 检查密码
    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    # 生成token
    def create_token(self, expiration=6000):
        print(key)
        s = Serializer(key, expires_in=expiration)
        return s.dumps({'id': self.id}).decode("ascii")


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
    time = db.Column(db.DateTime,default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __init__(self, author_id, title, content):
        self.author_id = author_id
        self.title = title
        self.content = content
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
    time = db.Column(db.DateTime,default=datetime.datetime.now, onupdate=datetime.datetime.now)
    comments = db.relationship('Article', backref='art')

    def __init__(self, fromId, name, content):
        self.fromId = fromId
        self.name = name
        self.content = content
    def to_dict(self):
        t = self.__dict__
        del t['_sa_instance_state'] 
        return t