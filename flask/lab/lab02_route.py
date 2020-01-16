# https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#unique-urls-redirection-behavior
# /가 뒤에 붙으면 폴더 개념.
# /가 붙어 있을 땐 빼고 호출해도 /를 붙여서 redirect해줌
@app.route('/projects/')
def projects():
    return 'The project page'

# /가 없으면 뒤에 붙였을 때 404
@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(debug = True)