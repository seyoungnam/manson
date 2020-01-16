# https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods
# https://mooneegee.blogspot.com/2017/10/python-flask-http-get-post.html
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

# HTTP 메소드
'''
[GET] (라우팅 기본 설정)
암호화되지 않은 form의 데이터를 서버로 전송합니다.
가장 흔하게 사용되는 메소드입니다.
[HEAD]
response body를 제외하고 GET과 동일합니다.
[POST]
HTML form 데이터를 서버로 전송합니다. POST 메소드로 전달받은 데이터는 서버에 cache되지 않습니다.
[PUT]
현재 표현되고 있는 대상 resource를 업로드된 컨텐츠로 교체합니다.	
[DELETE]
URL가 준 현재 표현되고 있는 대상 resource를 제거합니다.

=> Restful API 개발 가능
'''
# route 장식자의 methods 인자로 설정 바꿀 수 있음 (기본은 get)
@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST': # post 방식이면
      user = request.form['myName']
      # 전달 받은 request에서 form의 'myName'이라는 이름의 값을 받아서
      return redirect(url_for('success', name = user))
      # url for로 url을 만들어 redirect. name에는 앞서 form에서 추출한 user값을 넣음
   else:
      user = request.args.get('myName')
      # get 방식의 경우 주소에서 args 값을 받음
      return redirect(url_for('success', name = user))
  
if __name__ == '__main__':
    app.run(debug = True)