# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# mysql://username:password@server/db?charset=utf8
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/test?charset=utf8'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'test'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'} # 한글 깨짐 방지
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
