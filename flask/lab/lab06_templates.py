# https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
# https://mooneegee.blogspot.com/2017/10/python-flask-template-web-template.html
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    # render_template은 templates안에 있는 파일을 지정해서, 뒤에 parameter를 전달
    return render_template('lab06_template/hello.html', name = user)

'''
hello_score() 함수의 URL rule은 정수 매개변수를 받습니다.
전달받은 정수 인자는 score.html template로 다시 전달됩니다.
‘marks’라는 변수로 전달받은 숫자값은 조건문에서 지정한대로 비교됩니다.
50보다 큰지 작은지 확인한 후, HTML 스크립트가 조건적으로 표시됩니다.
'''
@app.route('/score/<int:score>')
def score(score):
   return render_template('lab06_template/score.html', marks = score)

# for문 사용
@app.route('/result')
def result():
  dict = {'phy':50,'che':60,'maths':70}
  return render_template('lab06_template/result.html', result = dict)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
# https://mooneegee.blogspot.com/2017/11/python-flask-static-files.html
# 외부 static 파일(css, js) 연결
@app.route('/external')
def external():
    return render_template('lab06_template/external.html')
if __name__ == '__main__':
   app.run(debug = True)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#redirects-and-errors
# 에러 핸들러(404)
@app.errorhandler(404)
def page_not_found(error):
    return render_template('lab06_template/page_not_found.html'), 404