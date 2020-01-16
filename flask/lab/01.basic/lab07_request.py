# https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object
# https://mooneegee.blogspot.com/2017/11/python-flask-form-template.html
from flask import Flask, render_template, request
app = Flask(__name__)

'''
Request Object
클라이언트 웹 페이지의 데이터는 global request object를 통해서 서버로 전달됩니다.
request 데이터를 처리하기 위해서는 Flask 모듈로부터 import되어야 합니다.

request 객체의 중요한 속성은 다음과 같습니다.
Form - form 매개변수를 key로, 그 값을 value로 하는 쌍을 보관하는 dictionary입니다.
args - URL 부분 중 물음표(?) 다음에 있는 query 문자열의 내용을 parse합니다.
Cookies - Cookies 이름과 그 값을 가지는 dictionary 객체입니다.
files - 업로드 파일과 관련된 데이터
method - 현재 request method
'''

'''
발동된 함수에 의해서 전달받은 Form 데이터는 dictionary 객체의 form에 수집할 수 있고,
그 데이터를 대응하는 웹 페이지를 보여줄 template으로 보낼 수 있습니다.
'''

@app.route('/')
def student():
   return render_template('lab07_request/student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("lab07_request/result.html",result = result)
