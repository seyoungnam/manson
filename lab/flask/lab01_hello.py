# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
# pip install Flask
from flask import Flask # Flask class 가져오기
app = Flask(__name__) # 객체 생성
# __name__은 모듈의 이름이 저장되는 변수

@app.route('/') # route() 장식자를 통해 URL과 함수를 매핑
def hello_world():
    return 'Hello, World!'

# export FLASK_APP=lab01_hello.py (Linux)
# set FLASK_APP=lab01_hello.py (Winodw)
# flask run | python -m flask run
# http://127.0.0.1:5000/ 
# flask run --host=0.0.0.0

if __name__ == '__main__':
    app.run(debug = True) # 디버그 모드로 실행