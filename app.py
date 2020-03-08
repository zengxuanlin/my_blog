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

# db = SQLAlchemy(app)


print('数据库地址::',getUrl())

#创建用户表


# class User(db.Model):
#     __tablename__ = 'users'
#     guid = str(uuid.uuid4()).replace('-', '')
#     id = db.Column(db.String(64), primary_key=True, default=guid)
#     username = db.Column(db.String(16))
#     password = db.Column(db.String(255))
#     age = db.Column(db.String(3))
#     address = db.Column(db.String(64))
#     nickName = db.Column(db.String(64))
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#     articles = db.relationship('Article', backref='articles')

#     def __init__(self, username, password, age, address, nick, role_id):
#         self.username = username
#         #加密
#         self.password = generate_password_hash(password)
#         self.age = age
#         self.address = address
#         self.nickName = nick
#         self.role_id = role_id

#     # 检查密码
#     def check_password(self, pwd):
#         return check_password_hash(self.password, pwd)

#     #生成token
#     def create_token(self, expiration = 600):
#         s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
#         return s.dumps({ 'id': self.id }).decode("ascii")


# #通过token 拿到user
# def get_user(token):
#     s = Serializer(app.config['SECRET_KEY'])
#     try:
#         data = s.loads(token)
#     except:
#         return None
#     return User.query.filter_by(id=data['id']).first()




# @app.route('/login', methods=['POST'])
# def login():
#     # request.headers['token']  可以拿到请求头里的token
#     if request.method == 'POST':
#         post_data = post_json()
#         try:
#             user = User.query.filter_by(username=post_data['username']).first()
#             if user is not None:
#                 hasCheck = user.check_password(post_data['password'])
#                 print(hasCheck)
#                 if hasCheck:
#                     token = user.create_token()
#                     return responseData('登陆成功',{'token':token})
#                 else:

#                     return responseData('密码输入错误')
#             else:
#                 return responseData('找不到该用户')
#         except:
#            print('ERROR')

#     if request.method == 'GET':
#         pass


# #发表博文  
# @app.route('/publishArticle',methods=['POST'])
# def publish():
#     if request.method == 'POST':
#         post_data = post_json()
 
#         token = request.headers['token']
#         zId = get_user(token).id
#         print(token)
#         current_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
#         current_day = time.strftime("%H:%M:%S",time.localtime(time.time()))
#         curren_time = '{} {}'.format(current_date,current_day)
#         artice = Article(zId,post_data['title'],post_data['content'],curren_time)
#         db.session.add(artice)
#         db.session.commit()
#         return responseData('博文发布成功')
#     if request.method == 'GET':
#         pass

# #获取全部文章列表

# @app.route('/allArticles')
# def all():
#     all = Article.query.all()
#     count = Article.query.count()
#     data = []
#     for item in all:
#         data.append({"title":item.title,"content":item.content,'createTime':item.time,'nickName':item.articles.nickName})
#     return responseData('列表获取成功',data)

# #角色表
         
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     roleName = db.Column(db.String(16), unique=True)

#     def __init__(self, rn):
#         self.roleName = rn

# # 文章表


# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True)
#     author_id = db.Column(db.String(64), db.ForeignKey('users.id'))
#     title = db.Column(db.String(64))
#     content = db.Column(db.Text)
#     time = db.Column(db.String(64))

#     def __init__(self, author_id, title, content, time):
#         self.author_id = author_id
#         self.title = title
#         self.time = time
#         self.content = content

# #
# class Comment(db.Model):
    # __tablename__ = 'comment'
    # id = db.Column(db.Integer, primary_key=True)
    # fromId = db.Column(db.Integer, db.ForeignKey('article.id'))
    # name = db.Column(db.String(64))
    # content = db.Column(db.String(64))
    # time = db.Column(db.String(64))
    
    # def __init__(self, fromId, name, content, time):
    #     self.fromId = fromId
    #     self.name = name
    #     self.content = content
    #     self.time = time




if __name__ == "__main__":
    app.register_blueprint(blog)
    app.run(debug=True)
