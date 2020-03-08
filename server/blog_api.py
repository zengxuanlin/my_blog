from flask import Blueprint, request, Flask
from utils import get_user, post_json
from models import *
from format import *
import time
blog = Blueprint('blog', __name__)

# 登陆
@blog.route('/login', methods=['POST'])
def login():
    # request.headers['token']  可以拿到请求头里的token
    if request.method == 'POST':
        post_data = post_json()
        user = User.query.filter_by(username=post_data['username']).first()
        if user is not None:
            hasCheck = user.check_password(post_data['password'])
            print(hasCheck)
            if hasCheck:
                token = user.create_token()

                return responseData('登陆成功', {'token': token})
            else:

                return responseData('密码输入错误')
        else:
            return responseData('找不到该用户')

    if request.method == 'GET':
        pass


# 发表
@blog.route('/publishArticle', methods=['POST'])
def publish():
    if request.method == 'POST':
        post_data = post_json()
        token = request.headers['token']
        try:
            uId = get_user(token).id
        except Exception as e:
            return responseData('token过期或者失效', None, False)
        else:
            artice = Article(uId, post_data['title'], post_data['content'],post_data['mdText'])
            db.session.add(artice)
            db.session.commit()
            return responseData('博文发布成功')

    if request.method == 'GET':
        pass

# 首页全部
@blog.route('/allArticles')
def all():
    all = Article.query.all()
    count = Article.query.count()
    _dict = {'list': []}
    for item in all:
        data = {"title": item.title, "content": item.content,
                'createTime': item.time, 'nickName': item.articles.nickName, 'commonts': []}
        _dict['list'].append(data)
        for c in item.art:
            data['commonts'].append(
                {'id': c.id, 'name': c.name, 'content': c.content, 'time': c.time})

    _dict['total'] = str(count)
    return responseData('列表获取成功', _dict)

# 列表
@blog.route('/getMyAllArticles')
def getMy():
    token = request.headers['token']
    try:
        uId = get_user(token).id
    except Exception as e:
        return responseData('token过期或者失效', None, False)
    else:
        arts = Article.query.filter_by(author_id=uId).all()
        total = Article.query.filter_by(author_id=uId).count()
        data = []
        for u in arts:
            data.append(u.to_dict())
        return responseData('获取成功', {'total': str(total), 'list': data})

# 详情
@blog.route('/articles/<id>')
def getDetail(id):
    try:
        art = Article.query.filter_by(id=id).first()
        total = Article.query.filter_by(id=id).count()
        author = User.query.filter_by(id=art.author_id).first()
        comments = []
        cs = art.art
        for item in cs:
            comments.append(item.to_dict())
        tmp = {'c': comments, 'text': {'artTitle': art.title,
                                       'artContent': art.content, 'time': art.time, 'author': author.nickName}}
        return responseData('获取成功', {'total': str(total), 'data': tmp})
    except Exception as e:
        print(e)
        return responseData(str(e), None, False)

# 编辑
@blog.route('/edit/<id>', methods=['POST'])
def edit(id):
    token = request.headers['token']
    post_data = post_json()
    try:
        uId = get_user(token).id
    except Exception as e:
        return responseData('token过期或者失效', None, False)
    else:
        art = Article.query.filter_by(id=id).first()
        art.title = post_data['title']
        art.content = post_data['content']
        db.session.commit()
        return responseData('修改成功', None,)