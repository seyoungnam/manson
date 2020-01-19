# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#simple-relationships
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8'
db = SQLAlchemy(app)

from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('posts', lazy=True))
    # category와 관계 짓기
    # lazy load 설정이 되어 있어, 조회 시 데이터베이스에서 불러온다
    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

'''
>>> from lab02_relationships import db
>>> db.create_all()
>>> from lab02_relationships import Category
>>> from lab02_relationships import Post

>>> py = Category(name='Python')
>>> Post(title='Hello Python!', body='Python is pretty cool', category=py)
>>> p = Post(title='Snakes', body='Ssssssss')
>>> py.posts.append(p)
>>> db.session.add(py)

Post 객체를 session에 추가 할 필요가 없다.
Category가 session의 일부이므로 관계를 통해 카테고리와 연관된 모든 오브젝트도 추가된다.
Db.session.add()가 이러한 오브젝트 작성 전후에 호출되는지는 중요하지 않다.
관계의 어느쪽에서든 연결을 수행 할 수 있으므로,
(Post에 category를 py를 넣던, Post를 작성 후 py에 넣던)
범주를 사용하여 게시물을 만들거나 범주의 게시물 목록에 추가 할 수 있다.

>>> py.posts
[<Post 'Hello Python!'>, <Post 'Snakes'>]

한 쿼리만으로 모든 카테고리와 관련된 게시물을 불러오고 싶다면 아래와 같이
>>> from sqlalchemy.orm import joinedload
>>> query = Category.query.options(joinedload('posts'))
>>> for category in query:
...     print category, category.posts
<Category u'Python'> [<Post u'Hello Python!'>, <Post u'Snakes'>]

종속 관계에 따른 검색을 하고 싶다면 with_parent 사용
>>> Post.query.with_parent(py).filter(Post.title != 'Snakes').all()
[<Post 'Hello Python!'>]
'''