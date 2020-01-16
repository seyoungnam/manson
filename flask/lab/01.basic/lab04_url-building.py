# https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building
# https://mooneegee.blogspot.com/2017/10/python-flask-url-building-urlfor.html
from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

# url_for를 통해 함수와 대응되는 url을 작성 
# url_for(함수의 이름, 함수 내의 변수 부분 or 패러미터로 추가)
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    
if __name__ == '__main__':
    app.run(debug = True)