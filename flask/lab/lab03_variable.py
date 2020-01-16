# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
from flask import Flask, escape
# escape 모듈 추가로 import
app = Flask(__name__)

# 꺾쇠(<>)를 통해 변수명 지정 가능
# <variable_name>
@app.route('/user/<username>')
def show_user_profile(username):
    # 입력한 유저 이름을 출력
    return 'User %s' % escape(username)
    # escape : &, <, >, ‘, ” 등 프로그래밍에서 쓰이는 문자들을 html에서 표시하기 위해서 사용

# 변수 타입 지정도 가능
# <converter:variable_name>
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 전달 받은 id 출력, id는 숫자
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # /path/ 이후에 표시된 subpath 출력
    return 'Subpath %s' % escape(subpath)

'''
string : 기본 타입. / 뺀 글자
int : 양의 정수
float : 양의 실수(소수점 표기)
path : /가 포함된 글자
'''

if __name__ == '__main__':
    app.run(debug = True)