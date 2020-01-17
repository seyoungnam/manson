# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# mysql+pymysql://username:password@server/db?charset=utf8 (mariadb 사용 가능)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8'
db = SQLAlchemy(app)

# python extension 설치 필요 
class User(db.Model):
    # __tablename__ = 'test' # 테이블 이름 설정
    # __table_args__ = {'mysql_collate': 'utf8_general_ci'} # 한글 깨짐 방지
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

'''
python 인터프리터 실행
>>> from lab01_model import db
db 클래스 내 정의된 테이블들 일괄 생성
>>> db.create_all()

User 클래스를 사용해서 create 진행
>>> from lab01_model import User
>>> admin = User(username='admin', email='admin@example.com')
>>> guest = User(username='guest', email='guest@example.com')

session에 추가 뒤 커밋
>>> db.session.add(admin)
>>> db.session.add(guest)
>>> db.session.commit()

read 진행
>>> User.query.all()
[<User u'admin'>, <User u'guest'>]
>>> User.query.filter_by(username='admin').first()
<User u'admin'>
'''